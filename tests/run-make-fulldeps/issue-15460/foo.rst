tests/run-make-fulldeps/issue-15460/foo.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "dylib"]

#[link(name = "foo", kind = "static")]
extern "C" {
    pub fn foo();
}


