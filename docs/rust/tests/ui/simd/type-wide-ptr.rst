tests/ui/simd/type-wide-ptr.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

#![feature(repr_simd)]

// error-pattern:monomorphising SIMD type `S` with a non-primitive-scalar (integer/float/pointer) element type `*mut [u8]`

#[repr(simd)]
struct S([*mut [u8]; 4]);

fn main() {
    let _v: Option<S> = None;
}


