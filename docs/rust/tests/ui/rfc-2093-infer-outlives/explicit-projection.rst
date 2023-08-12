tests/ui/rfc-2093-infer-outlives/explicit-projection.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

trait Trait<'x, T> where T: 'x {
    type Type;
}

#[rustc_outlives]
struct Foo<'a, A, B> where A: Trait<'a, B> //~ ERROR rustc_outlives
{
    foo: <A as Trait<'a, B>>::Type
}

fn main() {}


