tests/ui/issues/issue-5153.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    fn foo(self: Box<Self>);
}

impl Foo for isize {
    fn foo(self: Box<isize>) { }
}

fn main() {
    (&5isize as &dyn Foo).foo();
    //~^ ERROR: no method named `foo` found for reference `&dyn Foo` in the current scope
}


