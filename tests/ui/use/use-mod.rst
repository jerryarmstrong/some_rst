tests/ui/use/use-mod.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use foo::bar::{
    self,
//~^ ERROR `self` import can only appear once in an import list
    Bar,
    self
//~^ ERROR the name `bar` is defined multiple times
};

use {self};
//~^ ERROR `self` import can only appear in an import list with a non-empty prefix

mod foo {
    pub mod bar {
        pub struct Bar;
        pub struct Baz;
    }
}

fn main() {}


