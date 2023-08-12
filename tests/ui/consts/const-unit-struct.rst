tests/ui/consts/const-unit-struct.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

struct Foo;

static X: Foo = Foo;

pub fn main() {
    match X {
        Foo => {}
    }
}


