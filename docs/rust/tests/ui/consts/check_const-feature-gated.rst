tests/ui/consts/check_const-feature-gated.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

const ARR: [usize; 1] = [2];

fn main() {
    let _ = 5 << ARR[0];
}


