tests/ui/suggestions/struct-field-type-including-single-colon.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    struct A;
    mod bar {
        struct B;
    }
}

struct Foo {
    a: foo:A,
    //~^ ERROR found single colon in a struct field type path
    //~| expected `,`, or `}`, found `:`
}

struct Bar {
    b: foo::bar:B,
    //~^ ERROR found single colon in a struct field type path
    //~| expected `,`, or `}`, found `:`
}

fn main() {}


