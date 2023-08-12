tests/ui/const-generics/defaults/repr-c-issue-82792.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #82792.

// run-pass

#[repr(C)]
pub struct Loaf<T: Sized, const N: usize = 1> {
    head: [T; N],
    slice: [T],
}

fn main() {}


