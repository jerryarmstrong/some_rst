src/tools/clippy/tests/ui-toml/disallowed_macros/disallowed_macros.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:macros.rs

#![allow(unused)]

extern crate macros;

use serde::Serialize;

fn main() {
    println!("one");
    println!("two");
    cfg!(unix);
    vec![1, 2, 3];

    #[derive(Serialize)]
    struct Derive;

    let _ = macros::expr!();
    macros::stmt!();
    let macros::pat!() = 1;
    let _: macros::ty!() = "";
    macros::item!();

    eprintln!("allowed");
}

struct S;

impl S {
    macros::item!();
}

trait Y {
    macros::item!();
}

impl Y for S {
    macros::item!();
}


