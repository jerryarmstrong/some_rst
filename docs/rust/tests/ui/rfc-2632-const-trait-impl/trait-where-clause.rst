tests/ui/rfc-2632-const-trait-impl/trait-where-clause.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

#[const_trait]
trait Bar {}

trait Foo {
    fn a();
    fn b() where Self: ~const Bar;
    fn c<T: ~const Bar>();
}

fn test1<T: Foo>() {
    T::a();
    T::b();
    //~^ ERROR the trait bound
    T::c::<T>();
    //~^ ERROR the trait bound
}

fn test2<T: Foo + Bar>() {
    T::a();
    T::b();
    T::c::<T>();
}

fn main() {}


