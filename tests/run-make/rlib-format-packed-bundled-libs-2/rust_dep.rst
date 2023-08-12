tests/run-make/rlib-format-packed-bundled-libs-2/rust_dep.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[link(name = "native_dep.ext", kind = "static", modifiers = "+verbatim")]
extern "C" {
    fn native_f1() -> i32;
}

pub fn rust_dep() {
    unsafe {
        assert!(native_f1() == 1);
    }
}


