tests/ui/consts/non-scalar-cast.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// https://github.com/rust-lang/rust/issues/37448

fn main() {
    struct A;
    const FOO: &A = &(A as A);
    let _x = FOO;
}


