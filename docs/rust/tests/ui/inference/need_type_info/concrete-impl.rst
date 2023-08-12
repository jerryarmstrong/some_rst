tests/ui/inference/need_type_info/concrete-impl.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Ambiguous<A> {
    fn method() {}
}

struct One;
struct Two;
struct Struct;

impl Ambiguous<One> for Struct {}
impl Ambiguous<Two> for Struct {}

fn main() {
    <Struct as Ambiguous<_>>::method();
    //~^ ERROR type annotations needed
    //~| ERROR type annotations needed
}


