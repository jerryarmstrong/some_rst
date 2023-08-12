tests/ui/closures/binder/implicit-return.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(closure_lifetime_binder)]

fn main() {
    let _f = for<'a> |_: &'a ()| {};
    //~^ implicit types in closure signatures are forbidden when `for<...>` is present
}


