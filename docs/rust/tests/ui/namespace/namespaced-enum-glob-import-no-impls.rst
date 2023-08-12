tests/ui/namespace/namespaced-enum-glob-import-no-impls.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod m2 {
    pub enum Foo {
        A,
        B(isize),
        C { a: isize },
    }

    impl Foo {
        pub fn foo() {}
        pub fn bar(&self) {}
    }
}

mod m {
    pub use m2::Foo::*;
}

pub fn main() {
    use m2::Foo::*;

    foo(); //~ ERROR cannot find function `foo` in this scope
    m::foo(); //~ ERROR cannot find function `foo` in module `m`
    bar(); //~ ERROR cannot find function `bar` in this scope
    m::bar(); //~ ERROR cannot find function `bar` in module `m`
}


