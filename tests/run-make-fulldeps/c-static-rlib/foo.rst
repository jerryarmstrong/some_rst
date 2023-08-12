tests/run-make-fulldeps/c-static-rlib/foo.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

#[link(name = "cfoo", kind = "static")]
extern "C" {
    fn foo();
}

pub fn rsfoo() {
    unsafe { foo() }
}


