tests/ui/default-method-parsing.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

trait Foo {
    fn m(&self, _:isize) { }
}

pub fn main() { }


