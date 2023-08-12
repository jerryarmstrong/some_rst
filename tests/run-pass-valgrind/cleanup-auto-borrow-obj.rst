tests/run-pass-valgrind/cleanup-auto-borrow-obj.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This would previously leak the Box<Trait> because we wouldn't
// schedule cleanups when auto borrowing trait objects.
// This program should be valgrind clean.

static mut DROP_RAN: bool = false;

struct Foo;
impl Drop for Foo {
    fn drop(&mut self) {
        unsafe { DROP_RAN = true; }
    }
}


trait Trait { fn dummy(&self) { } }
impl Trait for Foo {}

pub fn main() {
    {
        let _x: &Trait = &*(Box::new(Foo) as Box<Trait>);
    }
    unsafe {
        assert!(DROP_RAN);
    }
}


