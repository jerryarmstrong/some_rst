tests/run-pass-valgrind/dst-dtor-3.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unsized_tuple_coercion)]

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
        let _x: Box<(i32, Trait)> = Box::<(i32, Foo)>::new((42, Foo));
    }
    unsafe {
        assert!(DROP_RAN);
    }
}


