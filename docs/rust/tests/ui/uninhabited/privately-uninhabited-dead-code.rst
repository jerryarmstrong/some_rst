tests/ui/uninhabited/privately-uninhabited-dead-code.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

#![deny(unused_variables)]

mod foo {
    enum Bar {}

    #[allow(dead_code)]
    pub struct Foo {
        value: Bar, // "privately" uninhabited
    }

    pub fn give_foo() -> Foo { panic!() }
}

fn main() {
    let a = 42;
    foo::give_foo();
    println!("Hello, {}", a); // ok: we can't tell that this code is dead
}


