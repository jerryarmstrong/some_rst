tests/ui/parser/recover-ref-dyn-mut.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the parser detects `&dyn mut`, offers a help message, and
// recovers.

fn main() {
    let r: &dyn mut Trait;
    //~^ ERROR: `mut` must precede `dyn`
    //~| HELP: place `mut` before `dyn`
    //~| ERROR: cannot find trait `Trait` in this scope [E0405]
}


