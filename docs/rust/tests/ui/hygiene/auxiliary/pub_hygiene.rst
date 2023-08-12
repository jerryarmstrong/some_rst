tests/ui/hygiene/auxiliary/pub_hygiene.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]

macro x() {
    pub struct MyStruct;
}

x!();


