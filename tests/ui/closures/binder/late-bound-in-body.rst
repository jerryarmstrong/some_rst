tests/ui/closures/binder/late-bound-in-body.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(closure_lifetime_binder)]

fn main() {
    let _ = for<'a> || -> () {
        let _: &'a bool = &true;
    };
}


