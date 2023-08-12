tests/ui/nll/type-alias-free-regions.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we don't assume that type aliases have the same type parameters
// as the type they alias and then panic when we see this.

type A<'a> = &'a isize;
type B<'a> = Box<A<'a>>;

struct C<'a> {
    f: Box<B<'a>>
}

trait FromBox<'a> {
    fn from_box(b: Box<B>) -> Self;
}

impl<'a> FromBox<'a> for C<'a> {
    fn from_box(b: Box<B>) -> Self {
        C { f: b } //~ ERROR
    }
}

trait FromTuple<'a> {
    fn from_tuple( b: (B,)) -> Self;
}

impl<'a> FromTuple<'a> for C<'a> {
    fn from_tuple(b: (B,)) -> Self {
        C { f: Box::new(b.0) } //~ ERROR
    }
}

fn main() {}


