tests/ui/typeck/nonexistent-field-not-ambiguous.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    val: MissingType,
    //~^ ERROR cannot find type `MissingType` in this scope
}

fn main() {
    Foo { val: Default::default() };
}


