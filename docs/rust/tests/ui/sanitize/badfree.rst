tests/ui/sanitize/badfree.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-sanitizer-support
// needs-sanitizer-address
//
// compile-flags: -Z sanitizer=address -O
//
// run-fail
// error-pattern: AddressSanitizer: SEGV

use std::ffi::c_void;

extern "C" {
    fn free(ptr: *mut c_void);
}

fn main() {
    unsafe {
        free(1 as *mut c_void);
    }
}


