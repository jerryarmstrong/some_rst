tests/ui/traits/safety-inherent-impl.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that inherent impls cannot be unsafe.

struct SomeStruct;

unsafe impl SomeStruct { //~ ERROR inherent impls cannot be unsafe
    fn foo(self) { }
}

fn main() { }


