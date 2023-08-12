tests/ui/unique/unique-rec.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct X { x: isize }

pub fn main() {
    let x: Box<_> = Box::new(X {x: 1});
    let bar = x;
    assert_eq!(bar.x, 1);
}


