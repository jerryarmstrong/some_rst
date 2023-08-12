tests/ui/unsized/maybe-bounds-where-cpass.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct S<T>(*const T) where T: ?Sized;


fn main() {
    let u = vec![1, 2, 3];
    let _s: S<[u8]> = S(&u[..]);
}


