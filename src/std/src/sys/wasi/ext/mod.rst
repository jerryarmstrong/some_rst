src/std/src/sys/wasi/ext/mod.rs
===============================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    #![deny(unsafe_op_in_unsafe_fn)]

pub mod ffi;
pub mod fs;
pub mod io;

/// A prelude for conveniently writing platform-specific code.
///
/// Includes all extension traits, and some important type definitions.
#[stable(feature = "rust1", since = "1.0.0")]
pub mod prelude {
    #[doc(no_inline)]
    #[stable(feature = "rust1", since = "1.0.0")]
    pub use crate::sys::ext::ffi::{OsStrExt, OsStringExt};
    #[doc(no_inline)]
    #[stable(feature = "rust1", since = "1.0.0")]
    pub use crate::sys::ext::fs::FileTypeExt;
    #[doc(no_inline)]
    #[stable(feature = "rust1", since = "1.0.0")]
    pub use crate::sys::ext::fs::{DirEntryExt, FileExt, MetadataExt, OpenOptionsExt};
    #[doc(no_inline)]
    #[stable(feature = "rust1", since = "1.0.0")]
    pub use crate::sys::ext::io::{AsRawFd, FromRawFd, IntoRawFd, RawFd};
}


