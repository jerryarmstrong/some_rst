library/std/src/os/hermit/mod.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![stable(feature = "rust1", since = "1.0.0")]

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


