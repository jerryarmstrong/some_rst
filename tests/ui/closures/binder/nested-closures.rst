tests/ui/closures/binder/nested-closures.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(closure_lifetime_binder)]

fn main() {
    for<'a> || -> () { for<'c> |_: &'a ()| -> () {}; };
}


