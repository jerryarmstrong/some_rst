tests/ui/resolve/filter-intrinsics.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    // Should suggest only `std::mem::size_of`
    let _ = size_of::<usize>();
    //~^ ERROR cannot find

    // Should suggest `std::intrinsics::fabsf64`,
    // since there is no non-intrinsic to suggest.
    let _ = fabsf64(1.0);
    //~^ ERROR cannot find
}


