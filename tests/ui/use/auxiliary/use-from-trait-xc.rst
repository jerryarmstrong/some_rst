tests/ui/use/auxiliary/use-from-trait-xc.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub use self::sub::{Bar, Baz};

pub trait Trait {
    fn foo(&self);
    type Assoc;
    const CONST: u32;
}

struct Foo;

impl Foo {
    pub fn new() {}

    pub const C: u32 = 0;
}

mod sub {
    pub struct Bar;

    impl Bar {
        pub fn new() {}
    }

    pub enum Baz {}

    impl Baz {
        pub fn new() {}
    }
}


