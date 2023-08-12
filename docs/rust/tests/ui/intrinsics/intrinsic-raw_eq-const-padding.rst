tests/ui/intrinsics/intrinsic-raw_eq-const-padding.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]
#![feature(const_intrinsic_raw_eq)]

const BAD_RAW_EQ_CALL: bool = unsafe {
    std::intrinsics::raw_eq(&(1_u8, 2_u16), &(1_u8, 2_u16))
//~^ ERROR evaluation of constant value failed
};

pub fn main() {
}


