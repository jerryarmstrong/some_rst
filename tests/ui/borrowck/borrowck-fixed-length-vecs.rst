tests/ui/borrowck/borrowck-fixed-length-vecs.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let x = [22];
    let y = &x[0];
    assert_eq!(*y, 22);
}


