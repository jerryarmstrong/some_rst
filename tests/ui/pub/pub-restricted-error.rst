tests/ui/pub/pub-restricted-error.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Bar(pub(()));

struct Foo {
    pub(crate) () foo: usize, //~ ERROR expected identifier
}

fn main() {}


