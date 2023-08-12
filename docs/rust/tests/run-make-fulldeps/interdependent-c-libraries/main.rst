tests/run-make-fulldeps/interdependent-c-libraries/main.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate foo;
extern crate bar;

fn main() {
    bar::doit();
}


