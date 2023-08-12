tests/ui/structs/auxiliary/struct_field_privacy.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct A {
    a: isize,
    pub b: isize,
}

pub struct B {
    pub a: isize,
    b: isize,
}


