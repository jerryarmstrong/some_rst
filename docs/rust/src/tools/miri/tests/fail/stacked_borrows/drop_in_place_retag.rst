src/tools/miri/tests/fail/stacked_borrows/drop_in_place_retag.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Test that drop_in_place mutably retags the entire place, even for a type that does not need
//! dropping, ensuring among other things that it is writeable

//@error-pattern: /retag .* for Unique permission .* only grants SharedReadOnly permission/

fn main() {
    unsafe {
        let x = 0u8;
        let x = core::ptr::addr_of!(x);
        core::ptr::drop_in_place(x.cast_mut());
    }
}


