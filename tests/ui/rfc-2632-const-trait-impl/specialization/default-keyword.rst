tests/ui/rfc-2632-const-trait-impl/specialization/default-keyword.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(const_trait_impl)]
#![feature(min_specialization)]

#[const_trait]
trait Foo {
    fn foo();
}

impl const Foo for u32 {
    default fn foo() {}
}

fn main() {}


