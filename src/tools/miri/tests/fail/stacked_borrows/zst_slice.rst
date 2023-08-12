src/tools/miri/tests/fail/stacked_borrows/zst_slice.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-strict-provenance
//@error-pattern: /retag .* tag does not exist in the borrow stack/

fn main() {
    unsafe {
        let a = [1, 2, 3];
        let s = &a[0..0];
        assert_eq!(s.len(), 0);
        assert_eq!(*s.get_unchecked(1), 2);
    }
}


