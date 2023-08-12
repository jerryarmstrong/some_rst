tests/run-make/native-link-modifier-verbatim-rustc/rust_dep.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    fn upstream_native_f() -> i32;
}

pub fn rust_dep() {
    unsafe {
        assert!(upstream_native_f() == 0);
    }
}


