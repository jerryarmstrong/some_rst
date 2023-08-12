tests/run-make-fulldeps/glibc-staticlib-args/library.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_mangle]
pub extern "C" fn args_check() {
    assert_ne!(std::env::args_os().count(), 0);
}


