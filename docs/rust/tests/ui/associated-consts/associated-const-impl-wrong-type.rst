tests/ui/associated-consts/associated-const-impl-wrong-type.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    const BAR: u32;
}

struct SignedBar;

impl Foo for SignedBar {
    const BAR: i32 = -1;
    //~^ ERROR implemented const `BAR` has an incompatible type for trait [E0326]
}

fn main() {}


