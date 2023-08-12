tests/run-make-fulldeps/extern-multiple-copies2/foo1.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

pub struct A;

pub fn foo1(a: A) {
    drop(a);
}


