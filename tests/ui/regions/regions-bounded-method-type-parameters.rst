tests/ui/regions/regions-bounded-method-type-parameters.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that explicit region bounds are allowed on the various
// nominal types (but not on other types) and that they are type
// checked.

struct Foo;

impl Foo {
    fn some_method<A:'static>(self) { }
}

fn caller<'a>(x: &isize) {
    Foo.some_method::<&'a isize>();
    //~^ ERROR lifetime may not live long enough
}

fn main() { }


