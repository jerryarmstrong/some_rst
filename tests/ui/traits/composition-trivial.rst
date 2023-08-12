tests/ui/traits/composition-trivial.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

trait Foo {
    fn foo(&self);
}

trait Bar : Foo {
    fn bar(&self);
}

pub fn main() {}


