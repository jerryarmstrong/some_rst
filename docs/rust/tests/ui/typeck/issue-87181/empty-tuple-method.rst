tests/ui/typeck/issue-87181/empty-tuple-method.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Bar<T> {
    bar: T
}

struct Foo();
impl Foo {
    fn foo(&self) { }
}

fn main() {
    let thing = Bar { bar: Foo };
    thing.bar.foo();
    //~^ ERROR no method named `foo` found for struct constructor `fn() -> Foo {Foo}` in the current scope [E0599]
}


