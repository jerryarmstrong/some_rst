tests/ui/suggestions/dont-suggest-doc-hidden-variant-for-enum/auxiliary/hidden-parent.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

extern crate core;

#[doc(hidden)]
pub mod __private {
    pub use core::option::Option::{self, None, Some};
}


