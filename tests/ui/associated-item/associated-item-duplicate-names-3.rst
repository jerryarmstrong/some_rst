tests/ui/associated-item/associated-item-duplicate-names-3.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //
// Before the introduction of the "duplicate associated type" error, the
// program below used to result in the "ambiguous associated type" error E0223,
// which is unexpected.

trait Foo {
    type Bar;
}

struct Baz;

impl Foo for Baz {
    type Bar = i16;
    type Bar = u16; //~ ERROR duplicate definitions
}

fn main() {
    let x: Baz::Bar = 5;
    //~^ ERROR ambiguous associated type
}


