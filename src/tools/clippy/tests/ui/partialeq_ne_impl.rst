src/tools/clippy/tests/ui/partialeq_ne_impl.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

struct Foo;

impl PartialEq for Foo {
    fn eq(&self, _: &Foo) -> bool {
        true
    }
    fn ne(&self, _: &Foo) -> bool {
        false
    }
}

struct Bar;

impl PartialEq for Bar {
    fn eq(&self, _: &Bar) -> bool {
        true
    }
    #[allow(clippy::partialeq_ne_impl)]
    fn ne(&self, _: &Bar) -> bool {
        false
    }
}

fn main() {}


