tests/ui/privacy/private-impl-method.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod a {
    pub struct Foo {
        pub x: isize
    }

    impl Foo {
        fn foo(&self) {}
    }
}

fn f() {
    impl a::Foo {
        fn bar(&self) {} // This should be visible outside `f`
    }
}

fn main() {
    let s = a::Foo { x: 1 };
    s.bar();
    s.foo();    //~ ERROR associated function `foo` is private
}


