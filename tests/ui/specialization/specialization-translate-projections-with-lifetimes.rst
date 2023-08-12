tests/ui/specialization/specialization-translate-projections-with-lifetimes.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(specialization)] //~ WARN the feature `specialization` is incomplete

trait Iterator {
    fn next(&self);
}

trait WithAssoc {
    type Item;
}

impl<'a> WithAssoc for &'a () {
    type Item = &'a u32;
}

struct Cloned<I>(#[allow(unused_tuple_struct_fields)] I);

impl<'a, I, T: 'a> Iterator for Cloned<I>
    where I: WithAssoc<Item=&'a T>, T: Clone
{
    fn next(&self) {}
}

impl<'a, I, T: 'a> Iterator for Cloned<I>
    where I: WithAssoc<Item=&'a T>, T: Copy
{

}

fn main() {
    Cloned(&()).next();
}


