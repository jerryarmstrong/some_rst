tests/run-pass-valgrind/dst-dtor-4.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unsized_tuple_coercion)]

static mut DROP_RAN: isize = 0;

struct Foo;
impl Drop for Foo {
    fn drop(&mut self) {
        unsafe { DROP_RAN += 1; }
    }
}

pub fn main() {
    {
        let _x: Box<(i32, [Foo])> = Box::<(i32, [Foo; 3])>::new((42, [Foo, Foo, Foo]));
    }
    unsafe {
        assert_eq!(DROP_RAN, 3);
    }
}


