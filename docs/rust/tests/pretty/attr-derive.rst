tests/pretty/attr-derive.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:derive-foo.rs
// pp-exact
// Testing that both the inner item and next outer item are
// preserved, and that the first outer item parsed in main is not
// accidentally carried over to each inner function

#[macro_use]
extern crate derive_foo;

#[derive(Foo)]
struct X;

#[derive(Foo)]
#[Bar]
struct Y;

#[derive(Foo)]
struct WithRef {
    x: X,
    #[Bar]
    y: Y,
}

#[derive(Foo)]
enum Enum {

    #[Bar]
    Asdf,
    Qwerty,
}

fn main() {}


