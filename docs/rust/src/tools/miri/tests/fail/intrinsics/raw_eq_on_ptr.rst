src/tools/miri/tests/fail/intrinsics/raw_eq_on_ptr.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(intrinsics)]

extern "rust-intrinsic" {
    fn raw_eq<T>(a: &T, b: &T) -> bool;
}

fn main() {
    let x = &0;
    unsafe { raw_eq(&x, &x) }; //~ERROR: `raw_eq` on bytes with provenance
}


