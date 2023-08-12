tests/ui/associated-types/associated-type-destructuring-assignment.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(more_qualified_paths)]

enum E { V() }

fn main() {
    <E>::V() = E::V(); // OK, destructuring assignment
    <E>::V {} = E::V(); // OK, destructuring assignment
}


