tests/ui/parser/recover-field-semi.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    foo: i32;
    //~^ ERROR struct fields are separated by `,`
}

union Bar { //~ ERROR
    foo: i32;
    //~^ ERROR union fields are separated by `,`
}

enum Baz {
    Qux { foo: i32; }
    //~^ ERROR struct fields are separated by `,`
}

fn main() {}


