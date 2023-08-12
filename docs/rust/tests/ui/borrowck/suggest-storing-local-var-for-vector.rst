tests/ui/borrowck/suggest-storing-local-var-for-vector.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut vec = vec![0u32; 420];
    vec[vec.len() - 1] = 123; //~ ERROR cannot borrow `vec` as immutable because it is also borrowed as mutable
}


