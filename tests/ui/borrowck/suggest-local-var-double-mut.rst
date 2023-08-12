tests/ui/borrowck/suggest-local-var-double-mut.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // See issue #77834.

#![crate_type = "lib"]

mod method_syntax {
    struct Foo;

    impl Foo {
        fn foo(&mut self, _: f32) -> i32 { todo!() }
        fn bar(&mut self) -> f32 { todo!() }
        fn baz(&mut self) {
            self.foo(self.bar()); //~ ERROR
        }
    }
}

mod fully_qualified_syntax {
    struct Foo;

    impl Foo {
        fn foo(&mut self, _: f32) -> i32 { todo!() }
        fn bar(&mut self) -> f32 { todo!() }
        fn baz(&mut self) {
            Self::foo(self, Self::bar(self)); //~ ERROR
        }
    }
}


