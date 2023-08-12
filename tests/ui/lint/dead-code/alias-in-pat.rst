tests/ui/lint/dead-code/alias-in-pat.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![deny(dead_code)]

fn main() {
    struct Foo<T> { x: T }
    type Bar = Foo<u32>;
    let spam = |Bar { x }| x != 0;
    println!("{}", spam(Foo { x: 10 }));
}


