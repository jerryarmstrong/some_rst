tests/ui/coherence/coherence-with-closure.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that encountering closures during coherence does not cause issues.
#![feature(type_alias_impl_trait)]
type OpaqueClosure = impl Sized;
fn defining_use() -> OpaqueClosure {
    || ()
}

struct Wrapper<T>(T);
trait Trait {}
impl Trait for Wrapper<OpaqueClosure> {}
impl<T: Sync> Trait for Wrapper<T> {}
//~^ ERROR conflicting implementations of trait `Trait` for type `Wrapper<OpaqueClosure>`

fn main() {}


