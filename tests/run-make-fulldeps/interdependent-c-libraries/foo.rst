tests/run-make-fulldeps/interdependent-c-libraries/foo.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

#[link(name = "foo", kind = "static")]
extern "C" {
    fn foo();
}

pub fn doit() {
    unsafe {
        foo();
    }
}


