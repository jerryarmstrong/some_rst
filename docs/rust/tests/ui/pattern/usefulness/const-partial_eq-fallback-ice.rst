tests/ui/pattern/usefulness/const-partial_eq-fallback-ice.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(warnings)]

struct MyType;

impl PartialEq<usize> for MyType {
    fn eq(&self, y: &usize) -> bool {
        true
    }
}

const CONSTANT: &&MyType = &&MyType;

fn main() {
    if let CONSTANT = &&MyType {
        //~^ ERROR must be annotated with `#[derive(PartialEq, Eq)]`
        println!("did match!");
    }
}


