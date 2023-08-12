tests/ui/macros/bang-after-name.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#[allow(unused_macros)]

macro_rules! foo! { //~ ERROR macro names aren't followed by a `!`
    () => {};
}

fn main() {}


