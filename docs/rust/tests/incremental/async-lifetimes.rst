tests/incremental/async-lifetimes.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: rpass1 rpass2
// edition:2021

// See https://github.com/rust-lang/rust/issues/98890

#![allow(unused)]

struct Foo;

impl Foo {
    async fn f(&self, _: &&()) -> &() {
        &()
    }
}

#[cfg(rpass2)]
enum Bar {}

fn main() {}


