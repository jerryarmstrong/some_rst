src/std/src/sys/windows/ext/raw.rs
==================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    //! Windows-specific primitives.

#![stable(feature = "raw_ext", since = "1.1.0")]

use crate::os::raw::c_void;

#[stable(feature = "raw_ext", since = "1.1.0")]
pub type HANDLE = *mut c_void;
#[cfg(target_pointer_width = "32")]
#[stable(feature = "raw_ext", since = "1.1.0")]
pub type SOCKET = u32;
#[cfg(target_pointer_width = "64")]
#[stable(feature = "raw_ext", since = "1.1.0")]
pub type SOCKET = u64;


