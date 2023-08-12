tests/ui/lifetimes/lifetime-errors/ex3-both-anon-regions-using-impl-items.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    fn foo<'a>(x: &mut Vec<&u8>, y: &u8);
}
impl Foo for () {
    fn foo(x: &mut Vec<&u8>, y: &u8) {
        x.push(y);
        //~^ ERROR lifetime may not live long enough
    }
}
fn main() {}


