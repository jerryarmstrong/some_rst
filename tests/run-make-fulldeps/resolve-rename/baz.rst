tests/run-make-fulldeps/resolve-rename/baz.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

extern crate bar;

pub fn baz() { bar::bar() }


