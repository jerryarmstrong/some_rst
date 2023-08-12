tests/ui/fn/implied-bounds-unnorm-associated-type-2.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

trait Trait {
    type Type;
}

impl<T> Trait for T {
    type Type = ();
}

fn f<'a, 'b>(_: <&'a &'b () as Trait>::Type)
where
    'a: 'a,
    'b: 'b,
{
}

fn g<'a, 'b>() {
    f::<'a, 'b>(());
    //~^ ERROR lifetime may not live long enough
}

fn main() {}


