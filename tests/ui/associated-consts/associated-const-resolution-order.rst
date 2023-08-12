tests/ui/associated-consts/associated-const-resolution-order.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct MyType;

impl MyType {
    const IMPL_IS_INHERENT: bool = true;
}

trait MyTrait {
    const IMPL_IS_INHERENT: bool;
    const IMPL_IS_ON_TRAIT: bool;
}

impl MyTrait for MyType {
    const IMPL_IS_INHERENT: bool = false;
    const IMPL_IS_ON_TRAIT: bool = true;
}

fn main() {
    // Check that the inherent impl is used before the trait, but that the trait
    // can still be accessed.
    assert!(<MyType>::IMPL_IS_INHERENT);
    assert!(!<MyType as MyTrait>::IMPL_IS_INHERENT);
    assert!(<MyType>::IMPL_IS_ON_TRAIT);
}


