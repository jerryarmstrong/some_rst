tests/ui/lint/let_underscore/let_underscore_drop.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![warn(let_underscore_drop)]

struct NontrivialDrop;

impl Drop for NontrivialDrop {
    fn drop(&mut self) {
        println!("Dropping!");
    }
}

fn main() {
    let _ = NontrivialDrop; //~WARNING non-binding let on a type that implements `Drop`
}


