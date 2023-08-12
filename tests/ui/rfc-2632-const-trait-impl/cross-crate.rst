tests/ui/rfc-2632-const-trait-impl/cross-crate.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: stock gated stocknc gatednc
// [gated] check-pass
#![cfg_attr(any(gated, gatednc), feature(const_trait_impl))]

// aux-build: cross-crate.rs
extern crate cross_crate;

use cross_crate::*;

fn non_const_context() {
    NonConst.func();
    Const.func();
}

const fn const_context() {
    #[cfg(any(stocknc, gatednc))]
    NonConst.func();
    //[stocknc]~^ ERROR: the trait bound
    //[gatednc]~^^ ERROR: the trait bound
    Const.func();
    //[stock]~^ ERROR: cannot call
}

fn main() {}


