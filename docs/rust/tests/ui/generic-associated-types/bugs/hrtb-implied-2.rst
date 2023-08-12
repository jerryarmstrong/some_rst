tests/ui/generic-associated-types/bugs/hrtb-implied-2.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail
// known-bug: unknown

// This gives us problems because `for<'a> I::Item<'a>: Debug` should mean "for
// all 'a where I::Item<'a> is WF", but really means "for all 'a possible"

trait LendingIterator: Sized {
    type Item<'a>
    where
        Self: 'a;
    fn next(&mut self) -> Self::Item<'_>;
}
fn fails<I: LendingIterator, F>(iter: &mut I, f: F) -> bool
where
    F: FnMut(I::Item<'_>),
{
    let mut iter2 = Eat(iter, f);
    let _next = iter2.next();
    true
}
impl<I: LendingIterator> LendingIterator for &mut I {
    type Item<'a> = I::Item<'a> where Self:'a;
    fn next(&mut self) -> Self::Item<'_> {
        (**self).next()
    }
}

struct Eat<I, F>(I, F);
impl<I: LendingIterator, F> Iterator for Eat<I, F>
where
    F: FnMut(I::Item<'_>),
{
    type Item = ();
    fn next(&mut self) -> Option<Self::Item> {
        None
    }
}

fn main() {}


