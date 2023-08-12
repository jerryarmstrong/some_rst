tests/ui/specialization/min_specialization/impl-on-nonexisting.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(min_specialization)]

trait Trait {}
impl Trait for NonExistent {}
//~^ ERROR cannot find type `NonExistent` in this scope

fn main() {}


