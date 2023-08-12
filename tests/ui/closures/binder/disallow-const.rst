tests/ui/closures/binder/disallow-const.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(closure_lifetime_binder)]

fn main() {
    for<const N: i32> || -> () {};
    //~^ ERROR only lifetime parameters can be used in this context
}


