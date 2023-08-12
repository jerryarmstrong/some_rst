tests/ui/lint/unused/must-use-box-from-raw.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #99269

// check-pass

#![warn(unused_must_use)]

unsafe fn free<T>(ptr: *mut T) {
    Box::from_raw(ptr); //~ WARNING unused return value
}

fn main() {}


