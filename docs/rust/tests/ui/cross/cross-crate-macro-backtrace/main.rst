tests/ui/cross/cross-crate-macro-backtrace/main.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:extern_macro_crate.rs
#[macro_use(myprintln, myprint)]
extern crate extern_macro_crate;

fn main() {
    myprintln!("{}");
    //~^ ERROR in format string
}


