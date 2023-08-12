tests/ui/impl-header-lifetime-elision/inherent-impl.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

struct Foo<'a>(&'a u8);

impl Foo<'_> {
    fn x() {}
}

fn main() {}


