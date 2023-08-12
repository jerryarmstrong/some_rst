tests/ui/consts/return-in-const-fn.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// https://github.com/rust-lang/rust/issues/43754

const fn foo(x: usize) -> usize {
    return x;
}
fn main() {
    [0; foo(2)];
}


