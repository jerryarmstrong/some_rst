tests/ui/traits/multidispatch-conditional-impl-not-considered.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that we correctly ignore the blanket impl
// because (in this case) `T` does not impl `Clone`.
//
// Issue #17594.

use std::cell::RefCell;

trait Foo {
    fn foo(&self) {}
}

impl<T> Foo for T where T: Clone {}

struct Bar;

impl Bar {
    fn foo(&self) {}
}

fn main() {
    let b = RefCell::new(Bar);
    b.borrow().foo();
}


