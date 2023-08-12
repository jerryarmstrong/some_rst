src/tools/clippy/tests/ui/needless_parens_on_range_literals.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// edition:2018

#![warn(clippy::needless_parens_on_range_literals)]
#![allow(clippy::almost_complete_range)]

fn main() {
    let _ = ('a')..=('z');
    let _ = 'a'..('z');
    let _ = (1.)..2.;
    let _ = (1.)..(2.);
    let _ = ('a')..;
    let _ = ..('z');
}


