tests/ui/generic-associated-types/issue-87429-specialization.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

#![feature(specialization)]
//~^ WARN incomplete

trait Family {
    type Member<'a>: for<'b> PartialEq<Self::Member<'b>>;
}

struct I32Family;

impl Family for I32Family {
    default type Member<'a> = i32;
}

struct Foo;
struct FooFamily;

impl Family for FooFamily {
    default type Member<'a> = Foo;
    //~^ ERROR can't compare
}

fn main() {}


