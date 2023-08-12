tests/ui/rustdoc/duplicate_doc_alias.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused_attributes)]

#[doc(alias = "A")]
#[doc(alias = "A")] //~ ERROR
#[doc(alias = "B")]
#[doc(alias("B"))] //~ ERROR
pub struct Foo;

fn main() {}


