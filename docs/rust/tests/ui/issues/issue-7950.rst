tests/ui/issues/issue-7950.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // tests the good error message, not "missing module Foo" or something else unexpected

struct Foo;

fn main() {
    Foo::bar();
    //~^ ERROR no function or associated item named `bar` found for struct `Foo`
}


