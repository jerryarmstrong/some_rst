tests/ui/generic-associated-types/parse/trait-path-expected-token.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait X {
    type Y<'a>;
}

fn f1<'a>(arg : Box<dyn X<Y = B = &'a ()>>) {}
    //~^ ERROR: expected one of `!`, `(`, `+`, `,`, `::`, `<`, or `>`, found `=`

fn main() {}


