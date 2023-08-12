tests/run-make-fulldeps/issue-28595/a.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

#[link(name = "a", kind = "static")]
extern "C" {
    pub fn a();
}


