tests/ui/array-slice-vec/infer_array_len.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // see issue #70529
struct A;

impl From<A> for [u8; 2] {
    fn from(a: A) -> Self {
        [0; 2]
    }
}

impl From<A> for [u8; 3] {
    fn from(a: A) -> Self {
        [0; 3]
    }
}


fn main() {
    let a = A;
    let [_, _] = a.into();
    //~^ ERROR type annotations needed
}


