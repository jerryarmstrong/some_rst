tests/ui/traits/inductive-overflow/simultaneous.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #33344, initial version. This example allowed
// arbitrary trait bounds to be synthesized.

trait Tweedledum: IntoIterator {}
trait Tweedledee: IntoIterator {}

impl<T: Tweedledum> Tweedledee for T {}
impl<T: Tweedledee> Tweedledum for T {}

trait Combo: IntoIterator {}
impl<T: Tweedledee + Tweedledum> Combo for T {}

fn is_ee<T: Combo>(t: T) {
    t.into_iter();
}

fn main() {
    is_ee(4);
    //~^ ERROR overflow evaluating the requirement `{integer}: Tweedle
}


