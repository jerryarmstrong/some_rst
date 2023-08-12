tests/ui/structs/suggest-private-fields.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:struct_field_privacy.rs

extern crate struct_field_privacy as xc;

use xc::B;

struct A {
    pub a: u32,
    b: u32,
}

fn main () {
    // external crate struct
    let k = B {
        aa: 20,
        //~^ ERROR struct `B` has no field named `aa`
        bb: 20,
        //~^ ERROR struct `B` has no field named `bb`
    };
    // local crate struct
    let l = A {
        aa: 20,
        //~^ ERROR struct `A` has no field named `aa`
        bb: 20,
        //~^ ERROR struct `A` has no field named `bb`
    };
}


