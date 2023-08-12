src/tools/clippy/tests/ui/crashes/match_same_arms_const.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(clippy::match_same_arms)]

/// Test for https://github.com/rust-lang/rust-clippy/issues/2427

const PRICE_OF_SWEETS: u32 = 5;
const PRICE_OF_KINDNESS: u32 = 0;
const PRICE_OF_DRINKS: u32 = 5;

pub fn price(thing: &str) -> u32 {
    match thing {
        "rolo" => PRICE_OF_SWEETS,
        "advice" => PRICE_OF_KINDNESS,
        "juice" => PRICE_OF_DRINKS,
        _ => panic!(),
    }
}

fn main() {}


