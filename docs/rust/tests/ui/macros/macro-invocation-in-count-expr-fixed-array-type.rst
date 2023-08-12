tests/ui/macros/macro-invocation-in-count-expr-fixed-array-type.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

macro_rules! four {
    () => (4)
}

fn main() {
    let _x: [u16; four!()];
}


