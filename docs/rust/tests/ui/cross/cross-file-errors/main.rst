tests/ui/cross/cross-file-errors/main.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_use]
mod underscore;

fn main() {
    underscore!();
    //~^ ERROR `_` can only be used on the left-hand side of an assignment
}


