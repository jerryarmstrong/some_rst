tests/ui/self/arbitrary_self_types_pin_lifetime_mismatch.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::pin::Pin;

struct Foo;

impl Foo {
    fn a(self: Pin<&Foo>, f: &Foo) -> &Foo { f }
    //~^ lifetime may not live long enough

    fn c(self: Pin<&Self>, f: &Foo, g: &Foo) -> (Pin<&Foo>, &Foo) { (self, f) }
    //~^ lifetime may not live long enough
}

type Alias<T> = Pin<T>;
impl Foo {
    fn bar<'a>(self: Alias<&Self>, arg: &'a ()) -> &() { arg }
    //~^ lifetime may not live long enough
}

fn main() {}


