tests/ui/union/union-nonrepresentable.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    union U { //~ ERROR recursive type `U` has infinite size
    a: u8,
    b: std::mem::ManuallyDrop<U>,
}

fn main() {}


