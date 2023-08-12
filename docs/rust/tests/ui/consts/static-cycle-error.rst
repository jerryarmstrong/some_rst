tests/ui/consts/static-cycle-error.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct Foo {
    foo: Option<&'static Foo>
}

static FOO: Foo = Foo {
    foo: Some(&FOO),
};

fn main() {}


