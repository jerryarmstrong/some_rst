tests/ui/parser/removed-syntax-field-semicolon.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
    bar: ();
    //~^ ERROR struct fields are separated by `,`
}

fn main() {}


