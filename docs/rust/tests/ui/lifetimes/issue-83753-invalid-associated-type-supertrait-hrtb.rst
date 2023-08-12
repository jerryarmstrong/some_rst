tests/ui/lifetimes/issue-83753-invalid-associated-type-supertrait-hrtb.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

struct Foo {}
impl Foo {
    fn bar(foo: Foo<Target = usize>) {}
    //~^ associated type bindings are not allowed here
}
fn main() {}


