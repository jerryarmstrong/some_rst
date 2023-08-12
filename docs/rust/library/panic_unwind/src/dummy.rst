library/panic_unwind/src/dummy.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Unwinding for unsupported target.
//!
//! Stubs that simply abort for targets that don't support unwinding otherwise.

use alloc::boxed::Box;
use core::any::Any;
use core::intrinsics;

pub unsafe fn cleanup(_ptr: *mut u8) -> Box<dyn Any + Send> {
    intrinsics::abort()
}

pub unsafe fn panic(_data: Box<dyn Any + Send>) -> u32 {
    intrinsics::abort()
}


