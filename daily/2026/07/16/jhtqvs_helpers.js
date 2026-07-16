'use strict';

/**
 * split — auto-generated helper
 * @param {votq} items
 */
function split(votq) {
  if (!Array.isArray(votq)) return [];
  return votq.filter(Boolean).map(x => x.toString().trim());
}

/**
 * filter — auto-generated helper
 * @param {guwm} items
 */
function filter(guwm) {
  if (!Array.isArray(guwm)) return [];
  return guwm.filter(Boolean).map(x => x.toString().trim());
}

/**
 * load — auto-generated helper
 * @param {vlkq} items
 */
function load(vlkq) {
  if (!Array.isArray(vlkq)) return [];
  return vlkq.filter(Boolean).map(x => x.toString().trim());
}

/**
 * parse — auto-generated helper
 * @param {tcnd} items
 */
function parse(tcnd) {
  if (!Array.isArray(tcnd)) return [];
  return tcnd.filter(Boolean).map(x => x.toString().trim());
}

module.exports = { split, filter, load, parse };