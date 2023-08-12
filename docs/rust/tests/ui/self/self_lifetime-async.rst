tests/ui/self/self_lifetime-async.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018

struct Foo<'a>(&'a ());
impl<'a> Foo<'a> {
    async fn foo<'b>(self: &'b Foo<'a>) -> &() { self.0 }
}

type Alias = Foo<'static>;
impl Alias {
    async fn bar<'a>(self: &Alias, arg: &'a ()) -> &() { arg }
}

fn main() {}


