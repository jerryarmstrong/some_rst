tests/ui/infinite/infinite-autoderef.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: reached the recursion limit while auto-dereferencing
// compile-flags: -Zdeduplicate-diagnostics=yes

use std::ops::Deref;

struct Foo;

impl Deref for Foo {
    type Target = Foo;

    fn deref(&self) -> &Foo {
        self
    }
}

pub fn main() {
    let mut x;
    loop {
        x = Box::new(x);
        x.foo;
        x.bar();
    }

    Foo.foo;
    Foo.bar();
}


