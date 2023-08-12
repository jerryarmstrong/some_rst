tests/ui/async-await/await-keyword/2018-edition-error.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
#![allow(non_camel_case_types)]

mod outer_mod {
    pub mod await { //~ ERROR expected identifier
        pub struct await; //~ ERROR expected identifier
    }
}
use self::outer_mod::await::await; //~ ERROR expected identifier
    //~^ ERROR expected identifier, found keyword `await`

macro_rules! await { () => {}; } //~ ERROR expected identifier, found keyword `await`

fn main() {
    await!(); //~ ERROR expected expression, found `)`
}


