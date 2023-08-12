tests/ui/issues/issue-24945-repeat-dash-opts.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// This test is just checking that we continue to accept `-g -g -O -O`
// as options to the compiler.

// compile-flags:-g -g -O -O
// ignore-asmjs wasm2js does not support source maps yet

fn main() {
    assert_eq!(1, 1);
}


