tests/ui/lint/warn-ctypes-inhibit.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
// compile-flags:-D improper-ctypes

// pretty-expanded FIXME #23616
#![allow(improper_ctypes)]

mod libc {
    extern "C" {
        pub fn malloc(size: isize) -> *const u8;
    }
}

pub fn main() {}


