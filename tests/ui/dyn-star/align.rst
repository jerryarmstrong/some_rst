tests/ui/dyn-star/align.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: normal over_aligned
//[normal] check-pass

#![feature(dyn_star)]
//~^ WARN the feature `dyn_star` is incomplete and may not be safe to use and/or cause compiler crashes

use std::fmt::Debug;

#[cfg_attr(over_aligned,      repr(C, align(1024)))]
#[cfg_attr(not(over_aligned), repr(C))]
#[derive(Debug)]
struct AlignedUsize(usize);

fn main() {
    let x = AlignedUsize(12) as dyn* Debug;
    //[over_aligned]~^ ERROR `AlignedUsize` needs to be a pointer-sized type
}


