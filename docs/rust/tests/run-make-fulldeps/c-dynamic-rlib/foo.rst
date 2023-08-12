tests/run-make-fulldeps/c-dynamic-rlib/foo.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

#[link(name = "cfoo")]
extern "C" {
    fn foo();
}

pub fn rsfoo() {
    unsafe { foo() }
}


