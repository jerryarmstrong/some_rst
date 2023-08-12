tests/run-make-fulldeps/issue64319/bar.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate foo;

pub fn bar() {
    foo::foo();
}


