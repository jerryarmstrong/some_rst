tests/ui/closures/2229_closure_analysis/run_pass/drop_then_use_fake_reads.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
// check-pass
#![feature(rustc_attrs)]

fn main() {
    let mut x = 1;
    let c = || {
        drop(&mut x);
        match x { _ => () }
    };
}


