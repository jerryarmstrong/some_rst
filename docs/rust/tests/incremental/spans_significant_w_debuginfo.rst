tests/incremental/spans_significant_w_debuginfo.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test makes sure that just changing a definition's location in the
// source file also changes its incr. comp. hash, if debuginfo is enabled.

// revisions:rpass1 rpass2

// ignore-asmjs wasm2js does not support source maps yet
// compile-flags: -g -Z query-dep-graph

#![feature(rustc_attrs)]
#![rustc_partition_codegened(module = "spans_significant_w_debuginfo", cfg = "rpass2")]

#[cfg(rpass1)]
pub fn main() {}

#[cfg(rpass2)]
#[rustc_clean(cfg = "rpass2")]
pub fn main() {}


