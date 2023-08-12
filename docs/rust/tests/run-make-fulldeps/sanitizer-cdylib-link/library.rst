tests/run-make-fulldeps/sanitizer-cdylib-link/library.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_mangle]
pub extern "C" fn overflow() {
    let xs = [0, 1, 2, 3];
    let _y = unsafe { *xs.as_ptr().offset(4) };
}


