tests/ui/unique/unique-decl-init.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let i: Box<_> = Box::new(1);
    let j = i;
    assert_eq!(*j, 1);
}


