tests/rustdoc/auxiliary/rustdoc-ffi.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]

extern "C" {
    // @has lib/fn.foreigner.html //pre 'pub unsafe fn foreigner(cold_as_ice: u32)'
    pub fn foreigner(cold_as_ice: u32);
}


