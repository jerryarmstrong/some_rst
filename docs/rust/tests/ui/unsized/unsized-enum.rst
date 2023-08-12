tests/ui/unsized/unsized-enum.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn is_sized<T:Sized>() { }
fn not_sized<T: ?Sized>() { }

enum Foo<U> { FooSome(U), FooNone }
fn foo1<T>() { not_sized::<Foo<T>>() } // Hunky dory.
fn foo2<T: ?Sized>() { not_sized::<Foo<T>>() }
//~^ ERROR the size for values of type
//
// Not OK: `T` is not sized.

fn main() { }


