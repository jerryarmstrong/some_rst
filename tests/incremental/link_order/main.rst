tests/incremental/link_order/main.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:my_lib.rs
// error-pattern: error: linking with
// revisions:cfail1 cfail2
// compile-flags:-Z query-dep-graph

// Tests that re-ordering the `-l` arguments used
// when compiling an external dependency does not lead to
// an 'unstable fingerprint' error.

extern crate my_lib;

fn main() {}


