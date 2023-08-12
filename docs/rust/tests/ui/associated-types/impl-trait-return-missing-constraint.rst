tests/ui/associated-types/impl-trait-return-missing-constraint.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    type Item;
}

trait Bar: Foo {}

struct S;

impl Foo for S {
    type Item = i32;
}
impl Bar for S {}

struct T;

impl Foo for T {
    type Item = u32;
}
impl Bar for T {}

fn bar() -> impl Bar {
    T
}

fn baz() -> impl Bar<Item = i32> {
    //~^ ERROR type mismatch resolving `<impl Bar as Foo>::Item == i32`
    bar()
}

fn main() {
    let _ = baz();
}


