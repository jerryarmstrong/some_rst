tests/ui/borrowck/immut-function-arguments.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f(y: Box<isize>) {
    *y = 5; //~ ERROR cannot assign
}

fn g() {
    let _frob = |q: Box<isize>| { *q = 2; }; //~ ERROR cannot assign
}

fn main() {}


