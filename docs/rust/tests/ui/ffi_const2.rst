tests/ui/ffi_const2.rs
======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(ffi_const, ffi_pure)]

extern "C" {
    #[ffi_pure] //~ ERROR `#[ffi_const]` function cannot be `#[ffi_pure]`
    #[ffi_const]
    pub fn baz();
}

fn main() {
    unsafe { baz() };
}


