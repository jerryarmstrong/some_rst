tests/ui/feature-gates/feature-gate-lang-items.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[lang = "foo"] //~ ERROR language items are subject to change
                //~^ ERROR definition of an unknown language item: `foo`
trait Foo {}

fn main() {}


