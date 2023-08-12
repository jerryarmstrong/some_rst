tests/ui/generics/generic-lifetime-trait-impl.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This code used to produce an ICE on the definition of trait Bar
// with the following message:
//
// Type parameter out of range when substituting in region 'a (root
// type=fn(Self) -> 'astr) (space=FnSpace, index=0)
//
// Regression test for issue #16218.

trait Bar<'a> {
    fn dummy(&'a self);
}

trait Foo<'a> {
    fn dummy(&'a self) { }
    fn bar<'b, T: Bar<'b>>(self) -> &'b str;
}

impl<'a> Foo<'a> for &'a str {
    fn bar<T: Bar<'a>>(self) -> &'a str { panic!() } //~ ERROR lifetime
}

fn main() {
}


