tests/ui/rfc-2632-const-trait-impl/attr-misuse.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

#[const_trait]
trait A {
    #[const_trait] //~ ERROR attribute should be applied
    fn foo(self);
}

#[const_trait] //~ ERROR attribute should be applied
fn main() {}


