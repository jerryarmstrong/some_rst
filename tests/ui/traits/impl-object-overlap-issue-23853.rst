tests/ui/traits/impl-object-overlap-issue-23853.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that we are able to compile the case where both a blanket impl
// and the object type itself supply the required trait obligation.
// In this case, the blanket impl for `Foo` applies to any type,
// including `Bar`, but the object type `Bar` also implicitly supplies
// this context.

trait Foo { fn dummy(&self) { } }

trait Bar: Foo { }

impl<T:?Sized> Foo for T { }

fn want_foo<B:?Sized+Foo>() { }

fn main() {
    want_foo::<dyn Bar>();
}


