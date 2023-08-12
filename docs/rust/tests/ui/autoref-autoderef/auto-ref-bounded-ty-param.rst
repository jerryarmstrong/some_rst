tests/ui/autoref-autoderef/auto-ref-bounded-ty-param.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
trait Foo {
    fn f(&self);
}

struct Bar {
    x: isize
}

trait Baz {
    fn g(&self);
}

impl<T:Baz> Foo for T {
    fn f(&self) {
        self.g();
    }
}

impl Baz for Bar {
    fn g(&self) {
        println!("{}", self.x);
    }
}

pub fn main() {
    let y = Bar { x: 42 };
    y.f();
}


