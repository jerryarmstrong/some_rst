tests/ui/error-codes/E0396-fixed.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_mut_refs)]

const REG_ADDR: *mut u8 = 0x5f3759df as *mut u8;

const VALUE: u8 = unsafe { *REG_ADDR };
//~^ ERROR evaluation of constant value failed

fn main() {
}


