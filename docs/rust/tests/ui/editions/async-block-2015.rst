tests/ui/editions/async-block-2015.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    async fn foo() {
//~^ ERROR `async fn` is not permitted in Rust 2015
//~| NOTE to use `async fn`, switch to Rust 2018 or later
//~| HELP pass `--edition 2021` to `rustc`
//~| NOTE for more on editions, read https://doc.rust-lang.org/edition-guide

    let x = async {};
    //~^ ERROR cannot find struct, variant or union type `async` in this scope
    //~| NOTE `async` blocks are only allowed in Rust 2018 or later
    let y = async { //~ NOTE `async` blocks are only allowed in Rust 2018 or later
        let x = 42;
        //~^ ERROR expected identifier, found keyword `let`
        //~| NOTE expected identifier, found keyword
        //~| HELP pass `--edition 2021` to `rustc`
        //~| NOTE for more on editions, read https://doc.rust-lang.org/edition-guide
        42
    };
    let z = async { //~ NOTE `async` blocks are only allowed in Rust 2018 or later
        42
        //~^ ERROR expected identifier, found `42`
        //~| NOTE expected identifier
        //~| HELP pass `--edition 2021` to `rustc`
        //~| NOTE for more on editions, read https://doc.rust-lang.org/edition-guide
    };
    y.await;
    z.await;
    x
}

fn main() {}


