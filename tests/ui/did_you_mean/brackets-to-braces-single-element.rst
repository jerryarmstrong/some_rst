tests/ui/did_you_mean/brackets-to-braces-single-element.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const A: [&str; 1] = { "hello" };
//~^ ERROR mismatched types

const B: &[u32] = &{ 1 };
//~^ ERROR mismatched types

const C: &&[u32; 1] = &&{ 1 };
//~^ ERROR mismatched types

fn main() {}


