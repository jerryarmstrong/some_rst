tests/ui/associated-types/point-at-type-on-obligation-failure.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Bar {
    type Ok;
    type Sibling: Bar2<Ok=Self::Ok>;
}
trait Bar2 {
    type Ok;
}

struct Foo;
struct Foo2;

impl Bar for Foo {
    type Ok = ();
    type Sibling = Foo2;
    //~^ ERROR type mismatch resolving `<Foo2 as Bar2>::Ok == ()`
}
impl Bar2 for Foo2 {
    type Ok = u32;
}

fn main() {}


