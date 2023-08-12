tests/ui/async-await/await-keyword/post_expansion_error.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

macro_rules! r#await {
    () => { println!("Hello, world!") }
}

fn main() {
    await!()
    //~^ ERROR expected expression, found `)`
}


