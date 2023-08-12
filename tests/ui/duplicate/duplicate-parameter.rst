tests/ui/duplicate/duplicate-parameter.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f(a: isize, a: isize) {}
//~^ ERROR identifier `a` is bound more than once in this parameter list

fn main() {
}


