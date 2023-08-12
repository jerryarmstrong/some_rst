tests/ui/typeck/issue-87181/tuple-field.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Bar<T> {
    bar: T
}

struct Foo(char, u16);
impl Foo {
    fn foo() { }
}

fn main() {
    let thing = Bar { bar: Foo };
    thing.bar.0;
    //~^ ERROR no field `0` on type `fn(char, u16) -> Foo {Foo}` [E0609]
}


