tests/ui/generic-associated-types/unsatified-item-lifetime-bound.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait X {
    type Y<'a: 'static>;
    //~^ WARNING unnecessary lifetime parameter
}

impl X for () {
    type Y<'a> = &'a ();
}

struct B<'a, T: for<'r> X<Y<'r> = &'r ()>> {
    f: <T as X>::Y<'a>,
    //~^ ERROR lifetime bound not satisfied
}

struct C<'a, T: X> {
    f: <T as X>::Y<'a>,
    //~^ ERROR lifetime bound not satisfied
}

struct D<'a> {
    f: <() as X>::Y<'a>,
    //~^ ERROR lifetime bound not satisfied
}

fn main() {}


