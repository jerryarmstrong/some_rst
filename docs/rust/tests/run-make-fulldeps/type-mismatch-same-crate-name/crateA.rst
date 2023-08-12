tests/run-make-fulldeps/type-mismatch-same-crate-name/crateA.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    pub struct Foo;
}

mod bar {
    pub trait Bar{}

    pub fn bar() -> Box<Bar> {
        unimplemented!()
    }
}

// This makes the publicly accessible path
// differ from the internal one.
pub use foo::Foo;
pub use bar::{Bar, bar};


