tests/ui/parser/dyn-trait-compatibility.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type A0 = dyn;
//~^ ERROR cannot find type `dyn` in this scope
type A1 = dyn::dyn;
//~^ ERROR use of undeclared crate or module `dyn`
type A2 = dyn<dyn, dyn>;
//~^ ERROR cannot find type `dyn` in this scope
//~| ERROR cannot find type `dyn` in this scope
//~| ERROR cannot find type `dyn` in this scope
type A3 = dyn<<dyn as dyn>::dyn>;
//~^ ERROR cannot find type `dyn` in this scope
//~| ERROR cannot find type `dyn` in this scope
//~| ERROR use of undeclared crate or module `dyn`

fn main() {}


