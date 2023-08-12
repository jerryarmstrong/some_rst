tests/run-pass-valgrind/osx-frameworks.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pretty-expanded FIXME #23616

#![feature(rustc_private)]

extern crate libc;

#[cfg(target_os = "macos")]
#[link(name = "CoreFoundation", kind = "framework")]
extern "C" {
    fn CFRunLoopGetTypeID() -> libc::c_ulong;
}

#[cfg(target_os = "macos")]
pub fn main() {
    unsafe {
        CFRunLoopGetTypeID();
    }
}

#[cfg(not(target_os = "macos"))]
pub fn main() {}


