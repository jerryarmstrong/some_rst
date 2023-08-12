tests/ui/consts/const-slice-oob.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const FOO: &'static[u32] = &[1, 2, 3];
const BAR: u32 = FOO[5];
//~^ index out of bounds: the length is 3 but the index is 5
//~| ERROR evaluation of constant value failed

fn main() {
    let _ = BAR;
}


