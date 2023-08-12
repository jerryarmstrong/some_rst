tests/ui/async-await/await-keyword/2015-edition-warning.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![allow(non_camel_case_types)]
#![deny(keyword_idents)]

mod outer_mod {
    pub mod await {
//~^ ERROR `await` is a keyword
//~| WARN this is accepted in the current edition
        pub struct await;
//~^ ERROR `await` is a keyword
//~| WARN this is accepted in the current edition
    }
}
use outer_mod::await::await;
//~^ ERROR `await` is a keyword
//~| ERROR `await` is a keyword
//~| WARN this is accepted in the current edition
//~| WARN this is accepted in the current edition

fn main() {
    match await { await => {} }
//~^ ERROR `await` is a keyword
//~| ERROR `await` is a keyword
//~| WARN this is accepted in the current edition
//~| WARN this is accepted in the current edition
}


