tests/ui/traits/issue-8153.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that duplicate methods in impls are not allowed

struct Foo;

trait Bar {
    fn bar(&self) -> isize;
}

impl Bar for Foo {
    fn bar(&self) -> isize {1}
    fn bar(&self) -> isize {2} //~ ERROR duplicate definitions
}

fn main() {
    println!("{}", Foo.bar());
}


