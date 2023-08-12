tests/ui/cross/cross-borrow-trait.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that cross-borrowing (implicitly converting from `Box<T>` to `&T`) is
// forbidden when `T` is a trait.

struct Foo;
trait Trait { fn foo(&self) {} }
impl Trait for Foo {}

pub fn main() {
    let x: Box<dyn Trait> = Box::new(Foo);
    let _y: &dyn Trait = x; //~ ERROR E0308
                            //~| expected reference `&dyn Trait`
                            //~| found struct `Box<dyn Trait>`
}


