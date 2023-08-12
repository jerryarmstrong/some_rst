tests/ui/wf/wf-fn-where-clause.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we check where-clauses on fn items.


#![allow(dead_code)]

trait ExtraCopy<T:Copy> { }

fn foo<T,U>() where T: ExtraCopy<U> //~ ERROR E0277
{
}

fn bar() where Vec<dyn Copy>:, {}
//~^ ERROR E0277
//~| ERROR E0038

struct Vec<T> {
    t: T,
}

fn main() { }


