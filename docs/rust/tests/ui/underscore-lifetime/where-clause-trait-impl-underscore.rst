tests/ui/underscore-lifetime/where-clause-trait-impl-underscore.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: rust2015 rust2018
//[rust2018] edition:2018

trait WithType<T> {}
trait WithRegion<'a> { }

trait Foo { }

impl<T> Foo for Vec<T>
where
    T: WithRegion<'_>
//[rust2015,rust2018]~^ ERROR `'_` cannot be used here
{ }

fn main() {}


