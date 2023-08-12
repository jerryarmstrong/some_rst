tests/ui/closures/binder/async-closure-with-binder.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
#![feature(closure_lifetime_binder)]
#![feature(async_closure)]
fn main() {
    for<'a> async || ();
    //~^ ERROR `for<...>` binders on `async` closures are not currently supported
    //~^^ ERROR implicit types in closure signatures are forbidden when `for<...>` is present
}


