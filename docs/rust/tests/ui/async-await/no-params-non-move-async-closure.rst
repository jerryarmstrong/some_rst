tests/ui/async-await/no-params-non-move-async-closure.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

#![feature(async_closure)]

fn main() {
    let _ = async |x: u8| {};
    //~^ ERROR `async` non-`move` closures with parameters are not currently supported
}


