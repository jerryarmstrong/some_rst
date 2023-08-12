tests/ui/unique/unique-in-vec.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let vect : Vec<Box<_>> = vec![Box::new(100)];
    assert_eq!(vect[0], Box::new(100));
}


