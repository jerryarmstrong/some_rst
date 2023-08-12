tests/ui/traits/object-does-not-impl-trait.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that an object type `Box<Foo>` is not considered to implement the
// trait `Foo`. Issue #5087.

trait Foo {}
fn take_foo<F:Foo>(f: F) {}
fn take_object(f: Box<dyn Foo>) { take_foo(f); }
//~^ ERROR `Box<dyn Foo>: Foo` is not satisfied
fn main() {}


