tests/ui/conservative_impl_trait.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #39872, #39553

fn will_ice(something: &u32) -> impl Iterator<Item = &u32> {
    //~^ ERROR `()` is not an iterator
}

fn main() {}


