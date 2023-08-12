tests/ui/rfc-2093-infer-outlives/explicit-dyn.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

trait Trait<'x, T> where T: 'x {
}

#[rustc_outlives]
struct Foo<'a, A> //~ ERROR rustc_outlives
{
    foo: Box<dyn Trait<'a, A>>
}

fn main() {}


