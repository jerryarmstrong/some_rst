tests/rustdoc/intra-doc/cross-crate/auxiliary/hidden.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "hidden_dep"]
#![deny(rustdoc::broken_intra_doc_links)]

#[doc(hidden)]
pub mod __reexport {
    pub use crate::*;
}

pub mod future {
    mod ready {

        /// Link to [`ready`](function@ready)
        pub struct Ready;
        pub fn ready() {}

    }
    pub use self::ready::{ready, Ready};

}


