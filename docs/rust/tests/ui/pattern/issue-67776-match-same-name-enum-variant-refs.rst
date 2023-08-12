tests/ui/pattern/issue-67776-match-same-name-enum-variant-refs.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test for issue #67776: binding named the same as enum variant
// should report an error even when matching against a reference type

#![allow(unused_variables)]
#![allow(non_snake_case)]

enum Foo {
    Bar,
    Baz,
}


fn fn1(e: Foo) {
    match e {
        Bar => {},
        //~^ ERROR named the same as one of the variants of the type `Foo`
        Baz => {},
        //~^ ERROR named the same as one of the variants of the type `Foo`
    }
}

fn fn2(e: &Foo) {
    match e {
        Bar => {},
        //~^ ERROR named the same as one of the variants of the type `Foo`
        Baz => {},
        //~^ ERROR named the same as one of the variants of the type `Foo`
    }
}

fn fn3(e: &mut &&mut Foo) {
    match e {
        Bar => {},
        //~^ ERROR named the same as one of the variants of the type `Foo`
        Baz => {},
        //~^ ERROR named the same as one of the variants of the type `Foo`
    }
}

fn main() {}


