tests/ui/imports/glob-cycles.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

mod foo {
    pub use bar::*;
    pub use main as f;
}

mod bar {
    pub use foo::*;
}

pub use foo::*;
pub use baz::*;
mod baz {
    pub use super::*;
}

pub fn main() {}


