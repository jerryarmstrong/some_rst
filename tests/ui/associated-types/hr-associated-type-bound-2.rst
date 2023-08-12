tests/ui/associated-types/hr-associated-type-bound-2.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait X<'a>
where
    for<'b> <Self as X<'b>>::U: Clone,
{
    type U: ?Sized;
    fn f(&self, x: &Self::U) {
        <Self::U>::clone(x);
    }
}

impl X<'_> for u32 //~ overflow evaluating the requirement `for<'b> u32: X<'b>`
where
    for<'b> <Self as X<'b>>::U: Clone,
{
    type U = str;
}

fn main() {
    1u32.f("abc");
}


