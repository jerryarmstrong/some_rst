tests/ui/consts/const-len-underflow-separate-spans.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that a constant-evaluation underflow highlights the correct
// spot (where the underflow occurred), while also providing the
// overall context for what caused the evaluation.

const ONE: usize = 1;
const TWO: usize = 2;
const LEN: usize = ONE - TWO;
//~^ ERROR constant

fn main() {
    let a: [i8; LEN] = unimplemented!();
//~^ constant
}


