tests/ui/traits/bound/on-structs-and-enums-xc1.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:on_structs_and_enums_xc.rs

extern crate on_structs_and_enums_xc;

use on_structs_and_enums_xc::{Bar, Foo, Trait};

fn main() {
    let foo = Foo {
        x: 3
    //~^ ERROR E0277
    };
    let bar: Bar<f64> = return;
    //~^ ERROR E0277
    let _ = bar;
}


