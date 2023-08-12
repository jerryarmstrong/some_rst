tests/ui/nll/unused-mut-issue-50343.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![deny(unused_mut)]
#![allow(unused_variables)] // for rustfix

fn main() {
    vec![(42, 22)].iter().map(|(mut x, _y)| ()).count();
    //~^ ERROR: variable does not need to be mutable
}


