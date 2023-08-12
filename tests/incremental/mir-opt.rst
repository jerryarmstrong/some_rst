tests/incremental/mir-opt.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // MIR optimizations can create expansions after the TyCtxt has been created.
// This test verifies that those expansions can be decoded correctly.

// revisions:rpass1 rpass2
// compile-flags: -Z query-dep-graph -Z mir-opt-level=3

fn main() {
    if std::env::var("a").is_ok() {
        println!("b");
    }
}


