tests/ui/array-slice-vec/vec-macro-no-std.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// ignore-emscripten no no_std executables

#![feature(lang_items, start, rustc_private)]
#![no_std]

extern crate std as other;

extern crate libc;

#[macro_use]
extern crate alloc;

use alloc::vec::Vec;

// Issue #16806

#[start]
fn start(_argc: isize, _argv: *const *const u8) -> isize {
    let x: Vec<u8> = vec![0, 1, 2];
    match x.last() {
        Some(&2) => (),
        _ => panic!(),
    }
    0
}


