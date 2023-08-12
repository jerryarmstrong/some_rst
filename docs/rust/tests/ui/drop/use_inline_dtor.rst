tests/ui/drop/use_inline_dtor.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:inline_dtor.rs

// pretty-expanded FIXME #23616

extern crate inline_dtor;

pub fn main() {
    let _x = inline_dtor::Foo;
}


