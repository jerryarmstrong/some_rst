src/tools/miri/tests/fail/stacked_borrows/illegal_write3.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let target = 42;
    // Make sure raw ptr with raw tag cannot mutate frozen location without breaking the shared ref.
    let r#ref = &target; // freeze
    let ptr = r#ref as *const _ as *mut _; // raw ptr, with raw tag
    unsafe { *ptr = 42 }; //~ ERROR: /write access .* only grants SharedReadOnly permission/
    let _val = *r#ref;
}


