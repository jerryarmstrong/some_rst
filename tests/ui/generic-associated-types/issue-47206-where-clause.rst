tests/ui/generic-associated-types/issue-47206-where-clause.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that this program doesn't cause the compiler to error without output.

trait Foo {
    type Assoc3<T>;
}

struct Bar;

impl Foo for Bar {
    type Assoc3<T> = Vec<T> where T: Iterator;
    //~^ ERROR impl has stricter requirements than trait
}

fn main() {}


