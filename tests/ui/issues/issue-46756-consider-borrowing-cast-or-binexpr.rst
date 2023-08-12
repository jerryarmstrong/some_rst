tests/ui/issues/issue-46756-consider-borrowing-cast-or-binexpr.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![allow(unused)]

fn light_flows_our_war_of_mocking_words(and_yet: &usize) -> usize {
    and_yet + 1
}

fn main() {
    let behold: isize = 2;
    let with_tears: usize = 3;
    light_flows_our_war_of_mocking_words(behold as usize);
    //~^ ERROR mismatched types [E0308]
    light_flows_our_war_of_mocking_words(with_tears + 4);
    //~^ ERROR mismatched types [E0308]
}


