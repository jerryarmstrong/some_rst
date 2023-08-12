tests/ui/suggestions/no-extern-crate-in-type.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:foo.rs

extern crate foo;

type Output = Option<Foo>; //~ ERROR cannot find type `Foo`

fn main() {}


