tests/ui/suggestions/suggest-on-bare-closure-call.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

#![feature(async_closure)]

fn main() {
    let _ = ||{}();
    //~^ ERROR expected function, found `()`

    let _ = async ||{}();
    //~^ ERROR expected function, found `()`
}


