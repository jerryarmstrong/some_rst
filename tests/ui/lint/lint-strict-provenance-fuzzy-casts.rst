tests/ui/lint/lint-strict-provenance-fuzzy-casts.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(strict_provenance)]
#![deny(fuzzy_provenance_casts)]

fn main() {
    let dangling = 16_usize as *const u8;
    //~^ ERROR strict provenance disallows casting integer `usize` to pointer `*const u8`
}


