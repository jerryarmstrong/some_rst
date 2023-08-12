tests/ui/mismatched_types/show_module.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod blah {
    pub mod baz {
        pub struct Foo;
    }
}

pub mod meh {
    pub struct Foo;
}

pub type Foo = blah::baz::Foo;

fn foo() -> Foo {
    meh::Foo
    //~^ ERROR mismatched types [E0308]
}

fn main() {}


