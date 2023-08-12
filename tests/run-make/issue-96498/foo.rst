tests/run-make/issue-96498/foo.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "cdylib"]

#[no_mangle]
extern "C" fn foo() {}


