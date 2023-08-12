tests/ui/async-await/issue-68523-start.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

#![feature(start)]

#[start]
pub async fn start(_: isize, _: *const *const u8) -> isize {
//~^ ERROR `start` is not allowed to be `async`
    0
}


