tests/ui/coherence/inter-crate-ambiguity-causes-notes.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S;

impl From<()> for S {
    fn from(x: ()) -> Self {
        S
    }
}

impl<I> From<I> for S
//~^ ERROR conflicting implementations of trait
where
    I: Iterator<Item = ()>,
{
    fn from(x: I) -> Self {
        S
    }
}

fn main() {}


