tests/ui/closures/closure-no-fn-5.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // When providing diagnostics about not being able to coerce a capturing-closure
// to fn type, we want to report only upto 4 captures.

fn main() {
    let a = 0u8;
    let b = 0u8;
    let c = 0u8;
    let d = 0u8;
    let e = 0u8;
    let bar: fn() -> u8 = || { a; b; c; d; e };
    //~^ ERROR mismatched types
}


