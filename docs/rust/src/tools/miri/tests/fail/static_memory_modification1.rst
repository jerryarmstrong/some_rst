src/tools/miri/tests/fail/static_memory_modification1.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Stacked Borrows detects that we are casting & to &mut and so it changes why we fail
//@compile-flags: -Zmiri-disable-stacked-borrows

static X: usize = 5;

#[allow(mutable_transmutes)]
fn main() {
    unsafe {
        *std::mem::transmute::<&usize, &mut usize>(&X) = 6; //~ ERROR: read-only
        assert_eq!(X, 6);
    }
}


