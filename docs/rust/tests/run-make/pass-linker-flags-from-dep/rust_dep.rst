tests/run-make/pass-linker-flags-from-dep/rust_dep.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    pub fn foo();
}

pub fn f() {
    unsafe {
        foo();
    }
}


