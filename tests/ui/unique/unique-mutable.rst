tests/ui/unique/unique-mutable.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let mut i: Box<_> = Box::new(0);
    *i = 1;
    assert_eq!(*i, 1);
}


