tests/run-make-fulldeps/symlinked-extern/baz.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate bar;
extern crate foo;

fn main() {
    bar::bar(foo::foo());
}


