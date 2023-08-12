tests/ui/rustdoc/feature-gate-doc_primitive.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#[doc(primitive = "usize")]
//~^ WARNING `doc(primitive)` should never have been stable
//~| WARNING hard error in a future release
/// Some docs
mod usize {}

fn main() {}


