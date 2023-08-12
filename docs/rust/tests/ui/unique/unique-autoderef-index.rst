tests/ui/unique/unique-autoderef-index.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let i: Box<_> = Box::new(vec![100]);
    assert_eq!((*i)[0], 100);
}


