tests/ui/closures/binder/disallow-ty.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(closure_lifetime_binder)]

fn main() {
    for<T> || -> () {};
    //~^ ERROR only lifetime parameters can be used in this context
}


