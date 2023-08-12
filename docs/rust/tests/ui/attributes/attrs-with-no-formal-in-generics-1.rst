tests/ui/attributes/attrs-with-no-formal-in-generics-1.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test checks variations on `<#[attr] 'a, #[oops]>`, where
// `#[oops]` is left dangling (that is, it is unattached, with no
// formal binding following it).

#![feature(rustc_attrs)]

struct RefIntPair<'a, 'b>(&'a u32, &'b u32);

impl<#[rustc_dummy] 'a, 'b, #[oops]> RefIntPair<'a, 'b> {
    //~^ ERROR trailing attribute after generic parameter
}

fn main() {}


