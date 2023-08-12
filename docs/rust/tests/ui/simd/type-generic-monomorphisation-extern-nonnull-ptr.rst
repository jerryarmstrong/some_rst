tests/ui/simd/type-generic-monomorphisation-extern-nonnull-ptr.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-emscripten

#![feature(extern_types)]
#![feature(repr_simd)]

use std::ptr::NonNull;

extern {
    type Extern;
}

#[repr(simd)]
struct S<T>(T);

#[inline(never)]
fn identity<T>(v: T) -> T {
    v
}

fn main() {
    let _v: S<[Option<NonNull<Extern>>; 4]> = identity(S([None; 4]));
}


