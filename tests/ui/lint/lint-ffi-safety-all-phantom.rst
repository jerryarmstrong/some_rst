tests/ui/lint/lint-ffi-safety-all-phantom.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This is a regression test for issue https://github.com/rust-lang/rust/issues/106629.
// It ensures that transparent types where all fields are PhantomData are marked as
// FFI-safe.

// check-pass

#[repr(transparent)]
#[derive(Copy, Clone)]
struct MyPhantom(core::marker::PhantomData<u8>);

#[repr(C)]
#[derive(Copy, Clone)]
pub struct Bar {
    pub x: i32,
    _marker: MyPhantom,
}

extern "C" {
    pub fn foo(bar: *mut Bar);
}

fn main() {}


