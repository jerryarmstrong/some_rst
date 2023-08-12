tests/ui/type-alias-impl-trait/unbounded_opaque_type.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]
type Opaque<T> = impl Sized;
fn defining<T>() -> Opaque<T> {}
struct Ss<'a, T>(&'a Opaque<T>);


fn test<'a, T>(_: Ss<'a, T>) {
    // test that we have an implied bound `Opaque<T>: 'a` from fn signature
    None::<&'a Opaque<T>>;
}

fn main() {}


