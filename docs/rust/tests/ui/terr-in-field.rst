tests/ui/terr-in-field.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    a: isize,
    b: isize,
}

struct Bar {
    a: isize,
    b: usize,
}

fn want_foo(f: Foo) {}
fn have_bar(b: Bar) {
    want_foo(b); //~  ERROR mismatched types
                 //~| expected struct `Foo`, found struct `Bar`
}

fn main() {}


