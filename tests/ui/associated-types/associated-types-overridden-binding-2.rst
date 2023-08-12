tests/ui/associated-types/associated-types-overridden-binding-2.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(trait_alias)]

trait I32Iterator = Iterator<Item = i32>;

fn main() {
    let _: &dyn I32Iterator<Item = u32> = &vec![42].into_iter();
    //~^ ERROR expected `IntoIter<u32>` to be an iterator that yields `i32`, but it yields `u32`
}


