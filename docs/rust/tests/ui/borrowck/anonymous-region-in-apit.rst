tests/ui/borrowck/anonymous-region-in-apit.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(anonymous_lifetime_in_impl_trait)]

trait Foo<T> {
    fn bar(self, baz: T);
}

fn qux(foo: impl Foo<&str>) {
    |baz: &str| foo.bar(baz);
    //~^ ERROR borrowed data escapes outside of closure
}

fn main() {}


