tests/ui/attributes/unknown-attr.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Unknown attributes fall back to unstable custom attributes.

#![feature(custom_inner_attributes)]

#![mutable_doc]
//~^ ERROR cannot find attribute `mutable_doc` in this scope

#[dance] mod a {}
//~^ ERROR cannot find attribute `dance` in this scope

#[dance] fn main() {}
//~^ ERROR cannot find attribute `dance` in this scope


