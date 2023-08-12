tests/ui/type-alias/issue-62364-self-ty-arg.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Struct<P1> {
    field: P1,
}

type Alias<'a> = Struct<&'a Self>;
//~^ ERROR cannot find type `Self` in this scope [E0411]

fn main() {}


