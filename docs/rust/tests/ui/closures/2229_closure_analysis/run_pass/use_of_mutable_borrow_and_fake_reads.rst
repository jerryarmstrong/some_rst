tests/ui/closures/2229_closure_analysis/run_pass/use_of_mutable_borrow_and_fake_reads.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
//check-pass
#![feature(rustc_attrs)]

fn main() {
    let mut x = 0;
    let c = || {
        &mut x; // mutable borrow of `x`
        match x { _ => () } // fake read of `x`
    };
}


