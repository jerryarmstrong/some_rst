tests/ui/wf/wf-complex-assoc-type.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait MyTrait {}
struct AssertMyTrait<T: MyTrait>(T);

trait HelperTrait {
    type MyItem;
}

impl HelperTrait for () {
    type MyItem = Option<((AssertMyTrait<bool>, u8))>; //~ ERROR the trait bound
}

fn main() {}


