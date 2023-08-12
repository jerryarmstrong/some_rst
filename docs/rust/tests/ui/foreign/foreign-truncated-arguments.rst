tests/ui/foreign/foreign-truncated-arguments.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -O
// Regression test for https://github.com/rust-lang/rust/issues/33868

#[repr(C)]
pub struct S {
    a: u32,
    b: f32,
    c: u32
}

#[no_mangle]
#[inline(never)]
pub extern "C" fn test(s: S) -> u32 {
    s.c
}

fn main() {
    assert_eq!(test(S{a: 0, b: 0.0, c: 42}), 42);
}


