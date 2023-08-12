tests/ui/consts/const_let_irrefutable.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

fn main() {}

const fn tup((a, b): (i32, i32)) -> i32 {
    a + b
}

const fn array([a, b]: [i32; 2]) -> i32 {
    a + b
}


