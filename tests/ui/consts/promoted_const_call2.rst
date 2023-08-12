tests/ui/consts/promoted_const_call2.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_precise_live_drops)]
pub const fn id<T>(x: T) -> T { x }
pub const C: () = {
    let _: &'static _ = &id(&String::new());
    //~^ ERROR: temporary value dropped while borrowed
    //~| ERROR: temporary value dropped while borrowed
    //~| ERROR: destructor of `String` cannot be evaluated at compile-time
};

fn main() {
    let _: &'static _ = &id(&String::new());
    //~^ ERROR: temporary value dropped while borrowed
    //~| ERROR: temporary value dropped while borrowed
}


