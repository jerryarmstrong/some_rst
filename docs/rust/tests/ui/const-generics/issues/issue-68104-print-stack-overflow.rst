tests/ui/const-generics/issues/issue-68104-print-stack-overflow.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:impl-const.rs
// run-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

extern crate impl_const;

use impl_const::*;

pub fn main() {
    let n = Num::<5>;
    n.five();
}


