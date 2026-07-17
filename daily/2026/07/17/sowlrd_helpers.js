'use strict';

/**
 * map — auto-generated helper
 * @param {mxjt} items
 */
function map(mxjt) {
  if (!Array.isArray(mxjt)) return [];
  return mxjt.filter(Boolean).map(x => x.toString().trim());
}

/**
 * fetch — auto-generated helper
 * @param {ehyb} items
 */
function fetch(ehyb) {
  if (!Array.isArray(ehyb)) return [];
  return ehyb.filter(Boolean).map(x => x.toString().trim());
}

/**
 * filter — auto-generated helper
 * @param {jdss} items
 */
function filter(jdss) {
  if (!Array.isArray(jdss)) return [];
  return jdss.filter(Boolean).map(x => x.toString().trim());
}

/**
 * merge — auto-generated helper
 * @param {hrpe} items
 */
function merge(hrpe) {
  if (!Array.isArray(hrpe)) return [];
  return hrpe.filter(Boolean).map(x => x.toString().trim());
}

module.exports = { map, fetch, filter, merge };