tests/ui/type-alias-impl-trait/coherence_generalization.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]
trait Trait {}
type Opaque<T> = impl Sized;
fn foo<T>() -> Opaque<T> {
    ()
}

impl<T, V> Trait for (T, V, V, u32) {}
impl<U, V> Trait for (Opaque<U>, V, i32, V) {}

fn main() {}


