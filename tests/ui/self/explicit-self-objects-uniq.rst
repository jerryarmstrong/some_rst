tests/ui/self/explicit-self-objects-uniq.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait Foo {
    fn f(self: Box<Self>);
}

struct S {
    x: isize
}

impl Foo for S {
    fn f(self: Box<S>) {
        assert_eq!(self.x, 3);
    }
}

pub fn main() {
    let x = Box::new(S { x: 3 });
    let y = x as Box<dyn Foo>;
    y.f();
}


