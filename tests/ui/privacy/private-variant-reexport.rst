tests/ui/privacy/private-variant-reexport.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod m1 {
    pub use ::E::V; //~ ERROR `V` is only public within the crate, and cannot be re-exported outside
}

mod m2 {
    pub use ::E::{V}; //~ ERROR `V` is only public within the crate, and cannot be re-exported outside
}

mod m3 {
    pub use ::E::V::{self}; //~ ERROR `V` is only public within the crate, and cannot be re-exported outside
}

#[deny(unused_imports)]
mod m4 {
    pub use ::E::*; //~ ERROR glob import doesn't reexport anything
}

enum E { V }

fn main() {}


