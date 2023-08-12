src/tools/miri/tests/fail/stacked_borrows/outdated_local.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut x = 0;
    let y: *const i32 = &x;
    x = 1; // this invalidates y by reactivating the lowermost uniq borrow for this local

    assert_eq!(unsafe { *y }, 1); //~ ERROR: /read access .* tag does not exist in the borrow stack/

    assert_eq!(x, 1);
}


