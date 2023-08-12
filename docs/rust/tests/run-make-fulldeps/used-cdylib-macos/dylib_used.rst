tests/run-make-fulldeps/used-cdylib-macos/dylib_used.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "cdylib"]

#[used]
static VERY_IMPORTANT_SYMBOL: u32 = 12345;


