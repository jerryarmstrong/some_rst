tests/ui/rust-2018/dyn-keyword.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2015
// run-rustfix

#![allow(unused_variables)]
#![deny(keyword_idents)]

fn main() {
    let dyn = (); //~ ERROR dyn
    //~^ WARN this is accepted in the current edition
}


