tests/run-make/native-link-modifier-verbatim-linker/main.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    fn local_native_f() -> i32;
}

pub fn main() {
    unsafe {
        assert!(local_native_f() == 0);
    };
}


