tests/ui/regions/regions-implied-bounds-projection-gap-3.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Along with the other tests in this series, illustrates the
// "projection gap": in this test, we know that `T::Foo: 'x`, and that
// is (naturally) enough to conclude that `T::Foo: 'x`.

// check-pass
#![allow(dead_code)]
#![allow(unused_variables)]

trait Trait1<'x> {
    type Foo;
}

// calling this fn should trigger a check that the type argument
// supplied is well-formed.
fn wf<T>() { }

fn func<'x, T:Trait1<'x>>(t: &'x T::Foo)
{
    wf::<&'x T::Foo>();
}


fn main() { }


