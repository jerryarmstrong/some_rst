tests/ui/associated-consts/associated-const-in-trait.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #29924

trait Trait {
    const N: usize;
}

impl dyn Trait {
    //~^ ERROR the trait `Trait` cannot be made into an object [E0038]
    const fn n() -> usize { Self::N }
}

fn main() {}


