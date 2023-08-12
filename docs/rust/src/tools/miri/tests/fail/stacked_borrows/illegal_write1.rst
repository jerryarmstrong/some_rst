src/tools/miri/tests/fail/stacked_borrows/illegal_write1.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let target = Box::new(42); // has an implicit raw
    let xref = &*target;
    {
        let x: *mut u32 = xref as *const _ as *mut _;
        unsafe { *x = 42 }; //~ ERROR: /write access .* tag only grants SharedReadOnly permission/
    }
    let _x = *xref;
}


