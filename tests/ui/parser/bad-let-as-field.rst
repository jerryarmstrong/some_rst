tests/ui/parser/bad-let-as-field.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    let: i32,
    //~^ ERROR expected identifier, found keyword
}

fn main() {}


