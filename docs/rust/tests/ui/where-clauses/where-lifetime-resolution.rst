tests/ui/where-clauses/where-lifetime-resolution.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Trait1<'a> {}
trait Trait2<'a, 'b> {}

fn f() where
    for<'a> dyn Trait1<'a>: Trait1<'a>, // OK
    (dyn for<'a> Trait1<'a>): Trait1<'a>,
    //~^ ERROR use of undeclared lifetime name `'a`
    for<'a> dyn for<'b> Trait2<'a, 'b>: Trait2<'a, 'b>,
    //~^ ERROR use of undeclared lifetime name `'b`
{}

fn main() {}


