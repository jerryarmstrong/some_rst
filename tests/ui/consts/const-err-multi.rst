tests/ui/consts/const-err-multi.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub const A: i8 = -i8::MIN;
//~^ ERROR constant
pub const B: i8 = A;
//~^ constant
pub const C: u8 = A as u8;
//~^ constant
pub const D: i8 = 50 - A;
//~^ constant

fn main() {
    let _ = (A, B, C, D);
}


