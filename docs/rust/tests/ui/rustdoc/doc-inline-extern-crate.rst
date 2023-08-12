tests/ui/rustdoc/doc-inline-extern-crate.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[doc(inline)]
//~^ ERROR conflicting
#[doc(no_inline)]
pub extern crate core;

// no warning
pub extern crate alloc;

fn main() {}


