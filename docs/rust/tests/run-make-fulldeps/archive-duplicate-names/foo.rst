tests/run-make-fulldeps/archive-duplicate-names/foo.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

#[link(name = "foo", kind = "static")]
extern "C" {
    fn foo();
    fn bar();
}

pub fn baz() {
    unsafe {
        foo();
        bar();
    }
}


