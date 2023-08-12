tests/ui/privacy/issue-75907_b.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test for diagnostic improvement issue #75907, extern crate
// aux-build:issue-75907.rs

extern crate issue_75907 as a;

use a::{make_bar, Bar, Foo};

fn main() {
    let Bar(x, y, z) = make_bar();
    //~^ ERROR cannot match against a tuple struct which contains private fields

    let Foo(x, y, z) = Foo::new();
    //~^ ERROR cannot match against a tuple struct which contains private fields
}


