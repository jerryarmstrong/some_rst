tests/ui/consts/const_let_refutable.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

const fn slice(&[a, b]: &[i32]) -> i32 {
    //~^ ERROR refutable pattern in function argument
    a + b
}


