tests/run-make-fulldeps/resolve-rename/bar.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

extern crate foo;

pub fn bar() { foo::foo() }


