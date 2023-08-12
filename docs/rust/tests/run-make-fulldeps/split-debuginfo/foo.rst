tests/run-make-fulldeps/split-debuginfo/foo.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Foo {
    x: u32,
}

impl Foo {
    pub fn print(&self) {
        println!("{}", self.x);
    }
}

pub fn make_foo(x: u32) -> Foo {
    Foo { x }
}

fn main() {}


