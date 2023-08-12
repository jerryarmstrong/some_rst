src/std/src/sys/hermit/ext/mod.rs
=================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    #![stable(feature = "rust1", since = "1.0.0")]
#![allow(missing_docs)]

pub mod ffi;

/// A prelude for conveniently writing platform-specific code.
///
/// Includes all extension traits, and some important type definitions.
#[stable(feature = "rust1", since = "1.0.0")]
pub mod prelude {
    #[doc(no_inline)]
    #[stable(feature = "rust1", since = "1.0.0")]
    pub use super::ffi::{OsStrExt, OsStringExt};
}


