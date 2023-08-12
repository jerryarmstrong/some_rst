tests/ui/nll/issue-50461-used-mut-from-moves.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![deny(unused_mut)]
#![allow(dead_code)]

struct Foo {
    pub value: i32
}

fn use_foo_mut(mut foo: Foo) {
    foo = foo;
    println!("{}", foo.value);
}

fn main() {
    use_foo_mut(Foo { value: 413 });
}


