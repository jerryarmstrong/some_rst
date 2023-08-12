tests/run-make-fulldeps/interdependent-c-libraries/bar.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

extern crate foo;

#[link(name = "bar", kind = "static")]
extern "C" {
    fn bar();
}

pub fn doit() {
    unsafe {
        bar();
    }
}


