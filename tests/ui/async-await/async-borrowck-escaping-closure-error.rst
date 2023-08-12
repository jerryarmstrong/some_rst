tests/ui/async-await/async-borrowck-escaping-closure-error.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
#![feature(async_closure)]
fn foo() -> Box<dyn std::future::Future<Output = u32>> {
    let x = 0u32;
    Box::new((async || x)())
    //~^ ERROR E0373
}

fn main() {
}


