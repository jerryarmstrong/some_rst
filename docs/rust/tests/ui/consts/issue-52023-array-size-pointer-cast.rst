tests/ui/consts/issue-52023-array-size-pointer-cast.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = [0; (&0 as *const i32) as usize]; //~ ERROR pointers cannot be cast to integers during const eval
}


