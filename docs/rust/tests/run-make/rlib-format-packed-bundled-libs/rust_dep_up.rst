tests/run-make/rlib-format-packed-bundled-libs/rust_dep_up.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[link(name = "native_dep_2", kind = "static")]
#[link(name = "native_dep_3", kind = "static")]
extern "C" {
    fn native_f2() -> i32;
    fn native_f3() -> i32;
}

pub fn rust_dep_up() {
    unsafe {
        assert!(native_f2() == 2);
        assert!(native_f3() == 3);
    }
}


