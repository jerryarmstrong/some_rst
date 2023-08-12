tests/ui/wf/wf-inherent-impl-where-clause.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we check where-clauses on inherent impls.

#![feature(associated_type_defaults)]

#![allow(dead_code)]

trait ExtraCopy<T:Copy> { }

struct Foo<T,U>(T,U);

impl<T,U> Foo<T,U> where T: ExtraCopy<U> //~ ERROR E0277
{
}


fn main() { }


