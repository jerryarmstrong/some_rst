tests/ui/feature-gates/feature-gate-arbitrary_self_types-raw-pointer.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;

impl Foo {
    fn foo(self: *const Self) {}
    //~^ ERROR `*const Foo` cannot be used as the type of `self` without
}

trait Bar {
    fn bar(self: *const Self);
    //~^ ERROR `*const Self` cannot be used as the type of `self` without
}

impl Bar for () {
    fn bar(self: *const Self) {}
    //~^ ERROR `*const ()` cannot be used as the type of `self` without
}

fn main() {}


