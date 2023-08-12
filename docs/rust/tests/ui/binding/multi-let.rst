tests/ui/binding/multi-let.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let x = 10;
    let y = x;
    assert_eq!(y, 10);
}


