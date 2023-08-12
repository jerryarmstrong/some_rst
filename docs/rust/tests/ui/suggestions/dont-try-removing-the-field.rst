tests/ui/suggestions/dont-try-removing-the-field.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]

struct Foo {
    foo: i32,
    bar: i32,
    baz: (),
}

fn use_foo(x: Foo) -> (i32, i32) {
    let Foo { foo, bar, baz } = x; //~ WARNING unused variable: `baz`
                                   //~| help: try ignoring the field
    return (foo, bar);
}

fn main() {}


