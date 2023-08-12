tests/ui/issues/issue-4228.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

struct Foo;

impl Foo {
    fn first() {}
}
impl Foo {
    fn second() {}
}

pub fn main() {
    Foo::first();
    Foo::second();
}


