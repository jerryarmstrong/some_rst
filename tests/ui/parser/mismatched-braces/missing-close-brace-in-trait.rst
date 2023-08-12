tests/ui/parser/mismatched-braces/missing-close-brace-in-trait.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait T {
    fn foo(&self);

pub(crate) struct Bar<T>();
//~^ ERROR struct is not supported in `trait`s or `impl`s

impl T for Bar<usize> {
//~^ ERROR implementation is not supported in `trait`s or `impl`s
fn foo(&self) {}
}

fn main() {} //~ ERROR this file contains an unclosed delimiter


