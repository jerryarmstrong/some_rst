tests/ui/traits/region-pointer-simple.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
trait Foo {
    fn f(&self) -> isize;
}

struct A {
    x: isize
}

impl Foo for A {
    fn f(&self) -> isize {
        println!("Today's number is {}", self.x);
        return self.x;
    }
}

pub fn main() {
    let a = A { x: 3 };
    let b = (&a) as &dyn Foo;
    assert_eq!(b.f(), 3);
}


