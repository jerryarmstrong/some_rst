tests/ui/rfc-2093-infer-outlives/self-dyn.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

trait Trait<'x, 's, T> where T: 'x,
      's: {
}

#[rustc_outlives]
struct Foo<'a, 'b, A> //~ ERROR rustc_outlives
{
    foo: Box<dyn Trait<'a, 'b, A>>
}

fn main() {}


