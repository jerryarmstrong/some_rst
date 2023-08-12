tests/ui/borrowck/borrowck-unary-move.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(x: Box<isize>) -> isize {
    let y = &*x;
    free(x); //~ ERROR cannot move out of `x` because it is borrowed
    *y
}

fn free(_x: Box<isize>) {
}

fn main() {
}


