src/std/src/sys/unix/ext/raw.rs
===============================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    //! Unix-specific primitives available on all unix platforms.

#![stable(feature = "raw_ext", since = "1.1.0")]
#![rustc_deprecated(
    since = "1.8.0",
    reason = "these type aliases are no longer supported by \
              the standard library, the `libc` crate on \
              crates.io should be used instead for the correct \
              definitions"
)]
#![allow(deprecated)]

#[stable(feature = "raw_ext", since = "1.1.0")]
#[allow(non_camel_case_types)]
pub type uid_t = u32;

#[stable(feature = "raw_ext", since = "1.1.0")]
#[allow(non_camel_case_types)]
pub type gid_t = u32;

#[stable(feature = "raw_ext", since = "1.1.0")]
#[allow(non_camel_case_types)]
pub type pid_t = i32;

#[doc(inline)]
#[stable(feature = "pthread_t", since = "1.8.0")]
pub use crate::sys::platform::raw::pthread_t;
#[doc(inline)]
#[stable(feature = "raw_ext", since = "1.1.0")]
pub use crate::sys::platform::raw::{blkcnt_t, time_t};
#[doc(inline)]
#[stable(feature = "raw_ext", since = "1.1.0")]
pub use crate::sys::platform::raw::{blksize_t, dev_t, ino_t, mode_t, nlink_t, off_t};


