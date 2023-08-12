tests/ui/underscore-imports/shadow.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that underscore imports don't cause glob imports to be unshadowed

mod a {
    pub use std::ops::Deref as Shadow;
}

mod b {
    pub use crate::a::*;
    macro_rules! m {
        ($i:ident) => { pub struct $i; }
    }
    m!(Shadow);
}

mod c {
    use crate::b::Shadow as _; // Only imports the struct

    fn f(x: &()) {
        x.deref(); //~ ERROR no method named `deref` found
    }
}

fn main() {}


