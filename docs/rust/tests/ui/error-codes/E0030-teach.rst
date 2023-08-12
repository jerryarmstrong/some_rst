tests/ui/error-codes/E0030-teach.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z teach

fn main() {
    match 5u32 {
        1000 ..= 5 => {}
        //~^ ERROR lower range bound must be less than or equal to upper
        //~| ERROR lower range bound must be less than or equal to upper
    }
}


