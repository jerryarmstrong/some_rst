tests/ui/associated-type-bounds/issue-102335-ty.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait T {
    type A: S<C<i32 = u32> = ()>;
    //~^ ERROR associated type bindings are not allowed here
}

trait Q {}

trait S {
    type C: Q;
}

fn main() {}


