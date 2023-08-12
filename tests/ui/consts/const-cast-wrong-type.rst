tests/ui/consts/const-cast-wrong-type.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const a: [u8; 3] = ['h' as u8, 'i' as u8, 0 as u8];
const b: *const i8 = &a as *const i8; //~ ERROR mismatched types

fn main() {
}


