tests/ui/specialization/defaultimpl/specialization-trait-not-implemented.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that:
// - default impls do not have to supply all items and
// - a default impl does not count as an impl (in this case, an incomplete default impl).

#![feature(specialization)] //~ WARN the feature `specialization` is incomplete

trait Foo {
    fn foo_one(&self) -> &'static str;
    fn foo_two(&self) -> &'static str;
}

struct MyStruct;

default impl<T> Foo for T {
    fn foo_one(&self) -> &'static str {
        "generic"
    }
}


fn main() {
    println!("{}", MyStruct.foo_one());
    //~^ ERROR the method
}


