tests/ui/async-await/no-const-async.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// compile-flags: --crate-type lib

pub const async fn x() {}
//~^ ERROR functions cannot be both `const` and `async`
//~| ERROR cycle detected


