src/tools/miri/tests/pass/constants.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const A: usize = *&5;

fn foo() -> usize {
    A
}

fn main() {
    assert_eq!(foo(), A);
}


