tests/ui/impl-trait/unactionable_diagnostic.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

pub trait Trait {}

pub struct Foo;

impl Trait for Foo {}

fn foo<'x, P>(
    _post: P,
    x: &'x Foo,
) -> &'x impl Trait {
    x
}

pub fn bar<'t, T>(
    //~^ HELP: consider adding an explicit lifetime bound...
    post: T,
    x: &'t Foo,
) -> &'t impl Trait {
    foo(post, x)
    //~^ ERROR: the parameter type `T` may not live long enough
}

fn main() {}


