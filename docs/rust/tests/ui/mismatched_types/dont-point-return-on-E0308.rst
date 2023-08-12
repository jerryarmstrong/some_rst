tests/ui/mismatched_types/dont-point-return-on-E0308.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

async fn f(_: &()) {}
//~^ NOTE function defined here
//~| NOTE
// Second note is the span of the underlined argument, I think...

fn main() {
    (|| async {
        Err::<(), ()>(())?;
        f(());
        //~^ ERROR mismatched types
        //~| NOTE arguments to this function are incorrect
        //~| NOTE expected `&()`, found `()`
        //~| HELP consider borrowing here
        Ok::<(), ()>(())
    })();
}


