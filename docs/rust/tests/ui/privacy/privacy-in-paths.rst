tests/ui/privacy/privacy-in-paths.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    pub use self::bar::S;
    mod bar {
        pub struct S;
        pub use baz;
    }

    trait T {
        type Assoc;
    }
    impl T for () {
        type Assoc = S;
    }
}

impl foo::S {
    fn f() {}
}

pub mod baz {
    fn f() {}

    fn g() {
        ::foo::bar::baz::f(); //~ERROR module `bar` is private
        ::foo::bar::S::f(); //~ERROR module `bar` is private
        <() as ::foo::T>::Assoc::f(); //~ERROR trait `T` is private
    }
}

fn main() {}


