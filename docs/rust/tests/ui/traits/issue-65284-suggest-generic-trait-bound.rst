tests/ui/traits/issue-65284-suggest-generic-trait-bound.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    fn foo(&self);
}

trait Bar {}

fn do_stuff<T : Bar>(t : T) {
    t.foo() //~ ERROR no method named `foo` found
}

fn main() {}


