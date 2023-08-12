src/tools/miri/tests/pass/partially-uninit.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem::{self, MaybeUninit};

#[repr(C)]
#[derive(Copy, Clone, Debug, PartialEq)]
struct Demo(bool, u16);

fn main() {
    unsafe {
        // Transmute-round-trip through a type with Scalar layout is lossless.
        // This is tricky because that 'scalar' is *partially* uninitialized.
        let x = Demo(true, 3);
        let y: MaybeUninit<u32> = mem::transmute(x);
        assert_eq!(x, mem::transmute(y));
    }
}


