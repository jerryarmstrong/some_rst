tests/ui/hygiene/impl_items-2.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]

trait Trait {
    fn foo() {}
}

macro trait_impl() {
    fn foo() {}
}

// Check that we error on multiple impl items that resolve to the same trait item.
impl Trait for i32 {
    trait_impl!();
    fn foo() {}
    //~^ ERROR duplicate definitions with name `foo`: [E0201]
}

struct Type;

// Check that we do not error with inherent impls.
impl Type {
    trait_impl!();
    fn foo() {}
}

fn main() {}


