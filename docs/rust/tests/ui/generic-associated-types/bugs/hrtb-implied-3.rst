tests/ui/generic-associated-types/bugs/hrtb-implied-3.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait LendingIterator {
    type Item<'a>
    where
        Self: 'a;
}

impl LendingIterator for &str {
    type Item<'a> = () where Self:'a;
}

fn trivial_bound<I>(_: I)
where
    I: LendingIterator,
    for<'a> I::Item<'a>: Sized,
{
}

fn fails(iter: &str) {
    trivial_bound(iter);
    //~^ borrowed data escapes
}

fn main() {}


