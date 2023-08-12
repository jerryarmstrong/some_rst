src/tools/clippy/tests/ui/auxiliary/doc_unsafe_macros.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! undocd_unsafe {
    () => {
        pub unsafe fn oy_vey() {
            unimplemented!();
        }
    };
}
#[macro_export]
macro_rules! undocd_safe {
    () => {
        pub fn vey_oy() {
            unimplemented!();
        }
    };
}


