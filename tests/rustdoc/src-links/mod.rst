tests/rustdoc/src-links/mod.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Dox
pub mod bar {

    /// Dox
    pub mod baz {
        /// Dox
        pub fn baz() { }
    }

    /// Dox
    pub trait Foobar { fn dummy(&self) { } }

    pub struct Foo { x: i32, y: u32 }

    pub fn prawns((a, b): (i32, u32), Foo { x, y }: Foo) { }
}

/// Dox
pub fn modfn() { }


