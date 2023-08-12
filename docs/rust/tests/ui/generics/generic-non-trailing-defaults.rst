tests/ui/generics/generic-non-trailing-defaults.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Heap;

struct Vec<A = Heap, T>(A, T);
//~^ ERROR generic parameters with a default must be trailing

struct Foo<A, B = Vec<C>, C>(A, B, C);
//~^ ERROR generic parameters with a default must be trailing
//~| ERROR generic parameters with a default cannot use

fn main() {}


