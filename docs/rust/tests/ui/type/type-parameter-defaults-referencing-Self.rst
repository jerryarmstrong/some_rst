tests/ui/type/type-parameter-defaults-referencing-Self.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test a default that references `Self` which is then used in an object type.
// Issue #18956.

trait Foo<T=Self> {
    fn method(&self);
}

fn foo(x: &dyn Foo) { }
//~^ ERROR the type parameter `T` must be explicitly specified

fn main() { }


