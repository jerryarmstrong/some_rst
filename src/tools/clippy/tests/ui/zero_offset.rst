src/tools/clippy/tests/ui/zero_offset.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(clippy::borrow_as_ptr)]
fn main() {
    unsafe {
        let m = &mut () as *mut ();
        m.offset(0);
        m.wrapping_add(0);
        m.sub(0);
        m.wrapping_sub(0);

        let c = &() as *const ();
        c.offset(0);
        c.wrapping_add(0);
        c.sub(0);
        c.wrapping_sub(0);

        let sized = &1 as *const i32;
        sized.offset(0);
    }
}


