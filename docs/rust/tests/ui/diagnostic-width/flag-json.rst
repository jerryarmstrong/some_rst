tests/ui/diagnostic-width/flag-json.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --diagnostic-width=20 --error-format=json

// This test checks that `-Z output-width` effects the JSON error output by restricting it to an
// arbitrarily low value so that the effect is visible.

fn main() {
    let _: () = 42;
    //~^ ERROR arguments to this function are incorrect
}


