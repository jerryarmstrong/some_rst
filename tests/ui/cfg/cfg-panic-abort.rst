tests/ui/cfg/cfg-panic-abort.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// compile-flags: -C panic=abort
// no-prefer-dynamic


#[cfg(panic = "unwind")]
pub fn bad() -> i32 { }

#[cfg(not(panic = "abort"))]
pub fn bad() -> i32 { }

#[cfg(panic = "some_imaginary_future_panic_handler")]
pub fn bad() -> i32 { }

#[cfg(panic = "abort")]
pub fn main() { }


