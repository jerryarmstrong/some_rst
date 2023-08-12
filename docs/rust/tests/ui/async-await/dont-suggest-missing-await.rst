tests/ui/async-await/dont-suggest-missing-await.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

// This test ensures we don't make the suggestion in bodies that aren't `async`.

fn take_u32(x: u32) {}

async fn make_u32() -> u32 {
    22
}

async fn dont_suggest_await_in_closure() {
    || {
        let x = make_u32();
        take_u32(x)
        //~^ ERROR mismatched types [E0308]
    };
}

fn main() {}


