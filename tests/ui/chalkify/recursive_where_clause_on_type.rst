tests/ui/chalkify/recursive_where_clause_on_type.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // FIXME(chalk): should fail, see comments
// check-fail
// compile-flags: -Z trait-solver=chalk

#![feature(trivial_bounds)]

trait Bar {
    fn foo();
}
trait Foo: Bar { }

struct S where S: Foo;

impl Foo for S {
}

fn bar<T: Bar>() {
    T::foo();
}

fn foo<T: Foo>() {
    bar::<T>()
}

fn main() {
    // For some reason, the error is duplicated...

    foo::<S>() //~ ERROR the type `S` is not well-formed
    //~^ ERROR the type `S` is not well-formed
}


