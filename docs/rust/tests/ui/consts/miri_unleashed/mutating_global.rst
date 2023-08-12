tests/ui/consts/miri_unleashed/mutating_global.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunleash-the-miri-inside-of-you

// Make sure we cannot mutate globals.

static mut GLOBAL: i32 = 0;

static MUTATING_GLOBAL: () = {
    unsafe {
        GLOBAL = 99
        //~^ ERROR could not evaluate static initializer
        //~| NOTE modifying a static's initial value
    }
};

fn main() {}


