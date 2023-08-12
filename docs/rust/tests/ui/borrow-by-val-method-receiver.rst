tests/ui/borrow-by-val-method-receiver.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait Foo {
    fn foo(self);
}

impl<'a> Foo for &'a [isize] {
    fn foo(self) {}
}

pub fn main() {
    let items = vec![ 3, 5, 1, 2, 4 ];
    items.foo();
}


