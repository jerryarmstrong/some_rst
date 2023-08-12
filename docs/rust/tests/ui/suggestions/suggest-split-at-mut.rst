tests/ui/suggestions/suggest-split-at-mut.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut foo = [1, 2, 3, 4];
    let a = &mut foo[2];
    let b = &mut foo[3]; //~ ERROR cannot borrow `foo[_]` as mutable more than once at a time
    *a = 5;
    *b = 6;
    println!("{:?} {:?}", a, b);
}


