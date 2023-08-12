tests/ui/generic-associated-types/anonymize-bound-vars.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
//
// regression test for #98702

trait Foo {
    type Assoc<T>;
}

impl Foo for () {
    type Assoc<T> = [T; 2*2];
}

fn main() {}


