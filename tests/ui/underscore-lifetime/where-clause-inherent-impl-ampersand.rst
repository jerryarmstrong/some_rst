tests/ui/underscore-lifetime/where-clause-inherent-impl-ampersand.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: rust2015 rust2018
//[rust2018] edition:2018

trait WithType<T> {}
trait WithRegion<'a> { }

struct Foo<T> {
    t: T
}

impl<T> Foo<T>
where
    T: WithType<&u32>
//[rust2015]~^ ERROR `&` without an explicit lifetime name cannot be used here
//[rust2018]~^^ ERROR `&` without an explicit lifetime name cannot be used here
{ }

fn main() {}


