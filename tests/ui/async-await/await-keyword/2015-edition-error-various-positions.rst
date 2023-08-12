tests/ui/async-await/await-keyword/2015-edition-error-various-positions.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(non_camel_case_types)]
#![deny(keyword_idents)]

mod outer_mod {
    pub mod await { //~ ERROR `await` is a keyword in the 2018 edition
    //~^ WARN this is accepted in the current edition
        pub struct await; //~ ERROR `await` is a keyword in the 2018 edition
        //~^ WARN this is accepted in the current edition
    }
}
use outer_mod::await::await; //~ ERROR `await` is a keyword in the 2018 edition
//~^ ERROR `await` is a keyword in the 2018 edition
//~^^ WARN this is accepted in the current edition
//~^^^ WARN this is accepted in the current edition

struct Foo { await: () }
//~^ ERROR `await` is a keyword in the 2018 edition
//~^^ WARN this is accepted in the current edition

impl Foo { fn await() {} }
//~^ ERROR `await` is a keyword in the 2018 edition
//~^^ WARN this is accepted in the current edition

macro_rules! await {
//~^ ERROR `await` is a keyword in the 2018 edition
//~^^ WARN this is accepted in the current edition
    () => {}
}

fn main() {
    await!(); //~ ERROR `await` is a keyword in the 2018 edition
    //~^ WARN this is accepted in the current edition

    match await { await => {} } //~ ERROR `await` is a keyword in the 2018 edition
    //~^ ERROR `await` is a keyword in the 2018 edition
    //~^^ WARN this is accepted in the current edition
    //~^^^ WARN this is accepted in the current edition
}


