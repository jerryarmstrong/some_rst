tests/ui/lifetimes/shadow.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<T>(T);

impl<'s> Foo<&'s u8> {
    fn bar<'s>(&self, x: &'s u8) {} //~ ERROR shadows a lifetime name
    fn baz(x: for<'s> fn(&'s u32)) {} //~ ERROR shadows a lifetime name
}

fn main() {}


