tests/ui/consts/miri_unleashed/auxiliary/static_cross_crate.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub static mut ZERO: [u8; 1] = [0];
pub static ZERO_REF: &[u8; 1] = unsafe { &ZERO };
pub static mut OPT_ZERO: Option<u8> = Some(0);


