tests/ui/suggestions/issue-64252-self-type.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test checks that a suggestion to add a `self: ` parameter name is provided
// to functions where this is applicable.

pub fn foo(Box<Self>) { }
//~^ ERROR expected one of `:`, `@`, or `|`, found `<`

struct Bar;

impl Bar {
    fn bar(Box<Self>) { }
    //~^ ERROR expected one of `:`, `@`, or `|`, found `<`
}

fn main() { }


