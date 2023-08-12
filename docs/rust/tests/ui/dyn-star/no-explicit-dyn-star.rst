tests/ui/dyn-star/no-explicit-dyn-star.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:dyn-star-foreign.rs

extern crate dyn_star_foreign;

fn main() {
    dyn_star_foreign::require_dyn_star_display(1usize as _);
    //~^ ERROR casting `usize` as `dyn* std::fmt::Display` is invalid
}


