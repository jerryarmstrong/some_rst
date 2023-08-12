tests/ui/async-await/drop-track-bad-field-in-fru.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zdrop-tracking
// edition: 2021

fn main() {}

async fn foo() {
    None { value: (), ..Default::default() }.await;
    //~^ ERROR `Option<_>` is not a future
    //~| ERROR variant `Option<_>::None` has no field named `value`
}


