tests/run-make-fulldeps/manual-link/foo.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

extern "C" {
    fn bar();
}

pub fn foo() {
    unsafe {
        bar();
    }
}


