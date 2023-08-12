tests/ui/lint/unused/issue-105061-should-lint.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(unused)]
#![deny(warnings)]

struct Inv<'a>(&'a mut &'a ());

trait Trait<'a> {}
impl<'b> Trait<'b> for for<'a> fn(Inv<'a>) {}

fn with_bound()
where
    for<'b> (for<'a> fn(Inv<'a>)): Trait<'b>, //~ ERROR unnecessary parentheses around type
{}

trait Hello<T> {}
fn with_dyn_bound<T>()
where
    (dyn Hello<(for<'b> fn(&'b ()))>): Hello<T> //~ ERROR unnecessary parentheses around type
{}

fn main() {
    with_bound();
    with_dyn_bound();
}


