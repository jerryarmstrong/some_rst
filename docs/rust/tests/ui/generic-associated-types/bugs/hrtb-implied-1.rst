tests/ui/generic-associated-types/bugs/hrtb-implied-1.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail
// known-bug: unknown

// This gives us problems because `for<'a> I::Item<'a>: Debug` should mean "for
// all 'a where I::Item<'a> is WF", but really means "for all 'a possible"

use std::fmt::Debug;

pub trait LendingIterator {
    type Item<'this>
    where
        Self: 'this;
}

pub struct WindowsMut<'x> {
    slice: &'x (),
}

impl<'y> LendingIterator for WindowsMut<'y> {
    type Item<'this> = &'this mut () where 'y: 'this;
}

fn print_items<I>(_iter: I)
where
    I: LendingIterator,
    for<'a> I::Item<'a>: Debug,
{
}

fn main() {
    let slice = &mut ();
    let windows = WindowsMut { slice };
    print_items::<WindowsMut<'_>>(windows);
}


