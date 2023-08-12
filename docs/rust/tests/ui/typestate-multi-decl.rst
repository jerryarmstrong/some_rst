tests/ui/typestate-multi-decl.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let (x, y) = (10, 20);
    let z = x + y;
    assert_eq!(z, 30);
}


