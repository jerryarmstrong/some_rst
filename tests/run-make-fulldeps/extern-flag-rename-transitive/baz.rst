tests/run-make-fulldeps/extern-flag-rename-transitive/baz.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

extern crate a;
extern crate bar;


