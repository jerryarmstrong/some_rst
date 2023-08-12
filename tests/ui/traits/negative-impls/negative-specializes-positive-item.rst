tests/ui/traits/negative-impls/negative-specializes-positive-item.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(specialization)] //~ WARN the feature `specialization` is incomplete
#![feature(negative_impls)]

// Negative impl for u32 cannot "specialize" the base impl.
trait MyTrait {
    fn foo();
}
impl<T> MyTrait for T {
    default fn foo() {}
}
impl !MyTrait for u32 {} //~ ERROR E0751

fn main() {}


