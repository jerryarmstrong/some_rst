tests/ui/writing-to-immutable-vec.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let v: Vec<isize> = vec![1, 2, 3];
    v[1] = 4; //~ ERROR cannot borrow `v` as mutable, as it is not declared as mutable
}


