tests/ui/borrowck/many-mutable-borrows.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let v = Vec::new(); //~ ERROR cannot borrow `v` as mutable, as it is not declared as mutable
    v.push(0);
    v.push(0);
    v.push(0);
    v.push(0);
    v.push(0);
    v.push(0);
    v.push(0);
    v.push(0);
    v.push(0);
    v.push(0);
    v.push(0);
    v.push(0);
    v.push(0);
    v.push(0);
    v.push(0);
}


