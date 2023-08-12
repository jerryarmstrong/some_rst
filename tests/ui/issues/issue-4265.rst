tests/ui/issues/issue-4265.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
      baz: usize
}

impl Foo {
    fn bar() {
        Foo { baz: 0 }.bar();
    }

    fn bar() { //~ ERROR duplicate definitions
    }
}

fn main() {}


