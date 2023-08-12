tests/ui/unique/unique-deref.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let i: Box<_> = Box::new(100);
    assert_eq!(*i, 100);
}


