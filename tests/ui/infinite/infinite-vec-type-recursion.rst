tests/ui/infinite/infinite-vec-type-recursion.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type X = Vec<X>;
//~^ ERROR cycle detected

fn main() { let b: X = Vec::new(); }


