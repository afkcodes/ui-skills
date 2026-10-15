/* Tiny SVG chart helpers that follow references/craft.md. No dependencies.
   Each returns an <svg class="chart"> element. Colours come from base.css classes. */
const NS = 'http://www.w3.org/2000/svg';
const el = (t, a = {}, ...kids) => { const n = document.createElementNS(NS, t); for (const k in a) n.setAttribute(k, a[k]); kids.forEach(k => n.append(k)); return n; };
const accent = () => (getComputedStyle(document.documentElement).getPropertyValue('--accent') || '#2f6df6').trim();
const txt = (x, y, s, a = {}) => { const t = el('text', { x, y, ...a }); t.textContent = s; return t; };

/** Bars with one selected bar + callout. opts: {labels, values, selected, fmt, h, w} */
export function bars({ labels, values, selected = -1, fmt = v => v, w = 600, h = 220 }) {
  const pad = { t: 36, r: 8, b: 30, l: 36 }, iw = w - pad.l - pad.r, ih = h - pad.t - pad.b;
  const max = Math.max(...values) * 1.1, slot = iw / values.length, bw = slot * 0.62;
  const svg = el('svg', { class: 'chart', viewBox: `0 0 ${w} ${h}` });
  const grid = el('g', { class: 'grid' }), axis = el('g', { class: 'axis' });
  for (let i = 0; i <= 4; i++) { const y = pad.t + ih - (ih * i) / 4; grid.append(el('line', { x1: pad.l, x2: w - pad.r, y1: y, y2: y })); axis.append(txt(pad.l - 8, y + 4, fmt(max * i / 4), { 'text-anchor': 'end' })); }
  svg.append(grid);
  values.forEach((v, i) => {
    const x = pad.l + slot * i + (slot - bw) / 2, bh = (v / max) * ih, y = pad.t + ih - bh, on = i === selected;
    svg.append(el('rect', { class: 'bar' + (on ? ' on' : ''), x, y, width: bw, height: bh, rx: Math.min(6, bw / 2) }));
    if (on) { const label = fmt(v), tw = label.length * 7 + 16; const tip = el('g', { class: 'tip' }); tip.append(el('rect', { x: x + bw / 2 - tw / 2, y: y - 30, width: tw, height: 22 })); tip.append(txt(x + bw / 2, y - 15, label, { 'text-anchor': 'middle' })); svg.append(tip); axis.append(el('rect', { class: 'on', x: x + bw / 2 - 16, y: h - 22, width: 32, height: 18, rx: 9 })); }
    axis.append(txt(x + bw / 2, h - 9, labels[i], { 'text-anchor': 'middle', class: on ? 'on' : '' }));
  });
  svg.append(axis); return svg;
}

/** Line/area with optional previous series and a cursor at `selected`. */
export function line({ labels, values, prev = null, selected = -1, fmt = v => v, w = 600, h = 220, area = true }) {
  const pad = { t: 36, r: 8, b: 30, l: 40 }, iw = w - pad.l - pad.r, ih = h - pad.t - pad.b;
  const all = prev ? values.concat(prev) : values, max = Math.max(...all) * 1.1, min = 0;
  const X = i => pad.l + (iw * i) / (values.length - 1), Y = v => pad.t + ih - ((v - min) / (max - min)) * ih;
  const path = vs => vs.map((v, i) => (i ? 'L' : 'M') + X(i).toFixed(1) + ' ' + Y(v).toFixed(1)).join(' ');
  const svg = el('svg', { class: 'chart', viewBox: `0 0 ${w} ${h}` });
  const grid = el('g', { class: 'grid' }), axis = el('g', { class: 'axis' });
  for (let i = 0; i <= 4; i++) { const y = pad.t + ih - (ih * i) / 4; grid.append(el('line', { x1: pad.l, x2: w - pad.r, y1: y, y2: y })); axis.append(txt(pad.l - 8, y + 4, fmt(max * i / 4), { 'text-anchor': 'end' })); }
  svg.append(grid);
  if (area) { const defs = el('defs'); const g = el('linearGradient', { id: 'af', x1: 0, y1: 0, x2: 0, y2: 1 }); g.append(el('stop', { offset: '0', 'stop-color': accent(), 'stop-opacity': .18 }), el('stop', { offset: '1', 'stop-color': accent(), 'stop-opacity': 0 })); defs.append(g); svg.append(defs); svg.append(el('path', { d: path(values) + ` L${X(values.length - 1)} ${pad.t + ih} L${X(0)} ${pad.t + ih} Z`, fill: 'url(#af)' })); }
  if (prev) svg.append(el('path', { class: 'line prev', d: path(prev) }));
  svg.append(el('path', { class: 'line', d: path(values) }));
  labels.forEach((l, i) => { if (i % Math.ceil(labels.length / 8) === 0 || i === labels.length - 1) axis.append(txt(X(i), h - 9, l, { 'text-anchor': 'middle' })); });
  if (selected >= 0) { const x = X(selected), y = Y(values[selected]); svg.append(el('line', { class: 'cursor', x1: x, x2: x, y1: pad.t, y2: pad.t + ih })); svg.append(el('circle', { class: 'pt', cx: x, cy: y, r: 4 })); const label = `${labels[selected]} · ${fmt(values[selected])}`, tw = label.length * 6.6 + 16; const tip = el('g', { class: 'tip' }); tip.append(el('rect', { x: Math.min(Math.max(x - tw / 2, pad.l), w - pad.r - tw), y: y - 34, width: tw, height: 22 })); tip.append(txt(Math.min(Math.max(x, pad.l + tw / 2), w - pad.r - tw / 2), y - 19, label, { 'text-anchor': 'middle' })); svg.append(tip); }
  svg.append(axis); return svg;
}

/** Ring gauge: value 0..1, centre label. */
export function ring({ value, label, sub, size = 140 }) {
  const r = (size - 12) / 2, c = 2 * Math.PI * r, svg = el('svg', { class: 'chart', viewBox: `0 0 ${size} ${size}`, style: `width:${size}px;height:${size}px` });
  svg.append(el('circle', { class: 'ring-track', cx: size / 2, cy: size / 2, r }));
  svg.append(el('circle', { class: 'ring', cx: size / 2, cy: size / 2, r, 'stroke-dasharray': `${c * value} ${c}`, transform: `rotate(-90 ${size / 2} ${size / 2})` }));
  const t = txt(size / 2, size / 2 + 6, label, { 'text-anchor': 'middle', style: 'font-size:26px;font-weight:600;letter-spacing:-.02em;fill:var(--fg)' }); svg.append(t);
  if (sub) svg.append(txt(size / 2, size / 2 + 24, sub, { 'text-anchor': 'middle', style: 'font-size:11px;fill:var(--fg-3)' }));
  return svg;
}

/** Sparkline for KPI tiles. */
export function spark({ values, w = 120, h = 28 }) {
  const max = Math.max(...values), min = Math.min(...values);
  const d = values.map((v, i) => (i ? 'L' : 'M') + ((w * i) / (values.length - 1)).toFixed(1) + ' ' + (h - 2 - ((v - min) / (max - min || 1)) * (h - 4)).toFixed(1)).join(' ');
  const svg = el('svg', { class: 'chart', viewBox: `0 0 ${w} ${h}`, style: `width:${w}px;height:${h}px` });
  svg.append(el('path', { class: 'line', d, 'stroke-width': 1.5 })); return svg;
}
