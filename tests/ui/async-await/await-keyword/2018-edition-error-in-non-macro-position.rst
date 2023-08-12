tests/ui/async-await/await-keyword/2018-edition-error-in-non-macro-position.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

#![allow(non_camel_case_types)]

mod outer_mod {
    pub mod await { //~ ERROR expected identifier, found keyword `await`
        pub struct await; //~ ERROR expected identifier, found keyword `await`
    }
}
use self::outer_mod::await::await; //~ ERROR expected identifier, found keyword `await`
//~^ ERROR expected identifier, found keyword `await`

struct Foo { await: () }
//~^ ERROR expected identifier, found keyword `await`

impl Foo { fn await() {} }
//~^ ERROR expected identifier, found keyword `await`

macro_rules! await {
//~^ ERROR expected identifier, found keyword `await`
    () => {}
}

fn main() {}


