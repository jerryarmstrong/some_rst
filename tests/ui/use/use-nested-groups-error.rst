tests/ui/use/use-nested-groups-error.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod a {
    pub mod b1 {
        pub enum C2 {}
    }

    pub enum B2 {}
}

use a::{b1::{C1, C2}, B2};
//~^ ERROR unresolved import `a::b1::C1`

fn main() {
    let _: C2;
    let _: B2;
}


