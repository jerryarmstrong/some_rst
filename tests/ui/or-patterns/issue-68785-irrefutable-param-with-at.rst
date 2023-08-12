tests/ui/or-patterns/issue-68785-irrefutable-param-with-at.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

enum MyEnum {
    FirstCase(u8),
    OtherCase(u16),
}

fn my_fn(x @ (MyEnum::FirstCase(_) | MyEnum::OtherCase(_)): MyEnum) {}

fn main() {
    my_fn(MyEnum::FirstCase(0));
}


