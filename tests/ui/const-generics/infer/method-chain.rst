tests/ui/const-generics/infer/method-chain.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;

impl Foo {
    fn bar(self) -> Foo {
        Foo
    }

    fn baz<const N: usize>(self) -> Foo {
        println!("baz: {}", N);
        Foo
    }
}

fn main() {
    Foo.bar().bar().bar().bar().baz(); //~ ERROR type annotations needed
}


