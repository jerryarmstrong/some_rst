tests/ui/structs-enums/struct-enum-ignoring-field-with-underscore.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Foo {
    Bar { bar: bool },
    Other,
}

fn main() {
    let foo = Some(Foo::Other);

    if let Some(Foo::Bar {_}) = foo {}
    //~^ ERROR expected identifier, found reserved identifier `_`
    //~| ERROR pattern does not mention field `bar` [E0027]
}


