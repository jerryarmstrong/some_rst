tests/ui/impl-trait/extra-item.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:extra-item.rs
// compile-flags:--extern extra_item

struct S;

impl extra_item::MyTrait for S {
    fn extra() {} //~ ERROR method `extra` is not a member of trait `extra_item::MyTrait`
}

fn main() {}


