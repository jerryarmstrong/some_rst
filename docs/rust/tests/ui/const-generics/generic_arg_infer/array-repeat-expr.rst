tests/ui/const-generics/generic_arg_infer/array-repeat-expr.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// To avoid having to `or` gate `_` as an expr.
#![feature(generic_arg_infer)]

fn foo() -> [u8; 3] {
    let x: [u8; _] = [0; _];
    x
}

fn main() {
    assert_eq!([0; _], foo());
}


