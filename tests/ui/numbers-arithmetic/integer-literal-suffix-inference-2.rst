tests/ui/numbers-arithmetic/integer-literal-suffix-inference-2.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

fn foo(_: *const ()) {}

fn main() {
    let a = 3;
    foo(&a as *const _ as *const ());
}


