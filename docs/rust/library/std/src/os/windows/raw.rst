library/std/src/os/windows/raw.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Windows-specific primitives.

#![stable(feature = "raw_ext", since = "1.1.0")]

use crate::os::raw::c_void;

#[stable(feature = "raw_ext", since = "1.1.0")]
pub type HANDLE = *mut c_void;
#[cfg(target_pointer_width = "32")]
#[doc(cfg(all()))]
#[stable(feature = "raw_ext", since = "1.1.0")]
pub type SOCKET = u32;
#[cfg(target_pointer_width = "64")]
#[doc(cfg(all()))]
#[stable(feature = "raw_ext", since = "1.1.0")]
pub type SOCKET = u64;


