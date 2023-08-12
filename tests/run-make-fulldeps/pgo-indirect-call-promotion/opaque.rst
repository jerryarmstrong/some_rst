tests/run-make-fulldeps/pgo-indirect-call-promotion/opaque.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="opaque"]
#![crate_type="rlib"]

#[no_mangle]
pub fn opaque_f1() {}
#[no_mangle]
pub fn opaque_f2() {}


