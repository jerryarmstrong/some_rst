tests/ui/typeck/issue-87181/enum-variant.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Bar<T> {
    bar: T
}

enum Foo{
    Tup()
}
impl Foo {
    fn foo(&self) { }
}

fn main() {
    let thing = Bar { bar: Foo::Tup };
    thing.bar.foo();
    //~^ ERROR no method named `foo` found for enum constructor `fn() -> Foo {Foo::Tup}` in the current scope [E0599]
}


