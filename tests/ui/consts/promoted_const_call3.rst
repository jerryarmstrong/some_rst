tests/ui/consts/promoted_const_call3.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub const fn id<T>(x: T) -> T { x }
pub const C: () = {
    let _: &'static _ = &String::new();
    //~^ ERROR: destructor of `String` cannot be evaluated at compile-time
    //~| ERROR: temporary value dropped while borrowed

    let _: &'static _ = &id(&String::new());
    //~^ ERROR: destructor of `String` cannot be evaluated at compile-time
    //~| ERROR: temporary value dropped while borrowed
    //~| ERROR: temporary value dropped while borrowed

    let _: &'static _ = &std::mem::ManuallyDrop::new(String::new());
    //~^ ERROR: temporary value dropped while borrowed
};

fn main() {
    let _: &'static _ = &String::new();
    //~^ ERROR: temporary value dropped while borrowed

    let _: &'static _ = &id(&String::new());
    //~^ ERROR: temporary value dropped while borrowed
    //~| ERROR: temporary value dropped while borrowed

    let _: &'static _ = &std::mem::ManuallyDrop::new(String::new());
    //~^ ERROR: temporary value dropped while borrowed
}


