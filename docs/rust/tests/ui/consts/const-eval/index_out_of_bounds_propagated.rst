tests/ui/consts/const-eval/index_out_of_bounds_propagated.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

fn main() {
    let array = [std::env::args().len()];
    array[1]; //~ ERROR operation will panic
}


