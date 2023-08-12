tests/ui/auxiliary/augmented_assignments.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ops::AddAssign;

pub struct Int(pub i32);

impl AddAssign<i32> for Int {
    fn add_assign(&mut self, _: i32) {
    }
}


