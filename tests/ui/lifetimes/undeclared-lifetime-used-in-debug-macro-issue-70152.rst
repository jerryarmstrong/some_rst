tests/ui/lifetimes/undeclared-lifetime-used-in-debug-macro-issue-70152.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Eq, PartialEq)]
struct Test {
    a: &'b str,
    //~^ ERROR use of undeclared lifetime name `'b`
    //~| ERROR use of undeclared lifetime name `'b`
}

trait T {
    fn foo(&'static self) {}
}

impl T for Test {
    fn foo(&'b self) {} //~ ERROR use of undeclared lifetime name `'b`
}

fn main() {}


