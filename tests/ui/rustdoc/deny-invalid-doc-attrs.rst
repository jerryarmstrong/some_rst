tests/ui/rustdoc/deny-invalid-doc-attrs.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(invalid_doc_attributes)]
//~^ NOTE defined here
#![doc(x)]
//~^ ERROR unknown `doc` attribute `x`
//~| WARNING will become a hard error
//~| NOTE see issue #82730
fn main() {}


