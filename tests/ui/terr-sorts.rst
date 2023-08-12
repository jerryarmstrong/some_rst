tests/ui/terr-sorts.rs
======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    a: isize,
    b: isize,
}

type Bar = Box<Foo>;

fn want_foo(f: Foo) {}
fn have_bar(b: Bar) {
    want_foo(b); //~  ERROR mismatched types
                 //~| expected struct `Foo`
                 //~| found struct `Box<Foo>`
}

fn main() {}


