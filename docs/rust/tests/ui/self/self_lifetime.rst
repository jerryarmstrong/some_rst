tests/ui/self/self_lifetime.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// https://github.com/rust-lang/rust/pull/60944#issuecomment-495346120

struct Foo<'a>(&'a ());
impl<'a> Foo<'a> {
    fn foo<'b>(self: &'b Foo<'a>) -> &() { self.0 }
}

type Alias = Foo<'static>;
impl Alias {
    fn bar<'a>(self: &Alias, arg: &'a ()) -> &() { arg }
}

fn main() {}


