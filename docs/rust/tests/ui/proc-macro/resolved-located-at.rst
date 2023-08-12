tests/ui/proc-macro/resolved-located-at.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:resolved-located-at.rs

#[macro_use]
extern crate resolved_located_at;

fn main() {
    resolve_located_at!(a b)
    //~^ ERROR expected error
    //~| ERROR mismatched types
}


