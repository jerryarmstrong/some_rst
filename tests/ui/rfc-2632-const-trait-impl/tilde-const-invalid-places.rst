tests/ui/rfc-2632-const-trait-impl/tilde-const-invalid-places.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]
#![feature(associated_type_bounds)]

struct TildeQuestion<T: ~const ?Sized>(std::marker::PhantomData<T>);
//~^ ERROR `~const` and `?` are mutually exclusive

fn main() {}


