src/tools/miri/tests/fail/stacked_borrows/mut_exclusive_violation2.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ptr::NonNull;

fn main() {
    unsafe {
        let x = &mut 0;
        let mut ptr1 = NonNull::from(x);
        let mut ptr2 = ptr1.clone();
        let raw1 = ptr1.as_mut();
        let _raw2 = ptr2.as_mut();
        let _val = *raw1; //~ ERROR: /read access .* tag does not exist in the borrow stack/
    }
}


