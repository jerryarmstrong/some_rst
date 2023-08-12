tests/ui/async-await/issues/non-async-enclosing-span.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

async fn do_the_thing() -> u8 {
    8
}
// #63398: point at the enclosing scope and not the previously seen closure
fn main() {  //~ NOTE this is not `async`
    let x = move || {};
    let y = do_the_thing().await; //~ ERROR `await` is only allowed inside `async` functions
    //~^ NOTE only allowed inside `async` functions and blocks
}


