tests/ui/consts/const-len-underflow-subspans.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that a constant-evaluation underflow highlights the correct
// spot (where the underflow occurred).

const ONE: usize = 1;
const TWO: usize = 2;

fn main() {
    let a: [i8; ONE - TWO] = unimplemented!();
    //~^ ERROR evaluation of constant value failed
    //~| attempt to compute `1_usize - 2_usize`, which would overflow
}


