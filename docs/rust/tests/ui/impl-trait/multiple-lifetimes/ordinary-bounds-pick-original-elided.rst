tests/ui/impl-trait/multiple-lifetimes/ordinary-bounds-pick-original-elided.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// build-pass (FIXME(62277): could be check-pass?

trait Trait<'a, 'b> {}
impl<T> Trait<'_, '_> for T {}

// Test case where we have elision in the impl trait and we have to
// pick the right region.

// Ultimately `Trait<'x, 'static>`.
fn upper_bounds1(a: &u8) -> impl Trait<'_, 'static> {
    (a, a)
}

// Ultimately `Trait<'x, 'x>`, so not really multiple bounds.
fn upper_bounds2(a: &u8) -> impl Trait<'_, '_> {
    (a, a)
}

// Kind of a weird annoying case.
fn upper_bounds3<'b>(a: &u8) -> impl Trait<'_, 'b> {
    (a, a)
}

fn main() {}


