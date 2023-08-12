tests/run-make-fulldeps/lto-no-link-whole-rlib/lib1.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

#[link(name = "foo", kind = "static")]
extern "C" {
    fn foo() -> i32;
}

pub fn foo1() -> i32 {
    unsafe { foo() }
}


