tests/ui/consts/const_fn_unsize.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(slice_ptr_len)]

use std::ptr::NonNull;

#[allow(unused)]
const fn test() {
    let _x = NonNull::<[i32; 0]>::dangling() as NonNull<[i32]>;
}

// Regression test for #75118.
pub const fn dangling_slice<T>() -> NonNull<[T]> {
    NonNull::<[T; 1]>::dangling()
}

const C: NonNull<[i32]> = dangling_slice();

fn main() {
    assert_eq!(C.as_ptr(), NonNull::<[i32; 1]>::dangling().as_ptr() as *mut _);
    assert_eq!(C.as_ptr().len(), 1);
}


