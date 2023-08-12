tests/run-make-fulldeps/extern-multiple-copies2/foo2.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

#[macro_use]
extern crate foo1;

pub fn foo2(a: foo1::A) {
    foo1::foo1(a);
}


