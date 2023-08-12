tests/ui/check-static-immutable-mut-slices.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks that immutable static items can't have mutable slices

static TEST: &'static mut [isize] = &mut [];
//~^ ERROR mutable references are not allowed

pub fn main() { }


