tests/ui/parser/mismatched-braces/missing-close-brace-in-impl-trait.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

impl T for () { //~ ERROR cannot find trait `T` in this scope

fn foo(&self) {}

trait T { //~ ERROR trait is not supported in `trait`s or `impl`s
    fn foo(&self);
}

pub(crate) struct Bar<T>(); //~ ERROR struct is not supported in `trait`s or `impl`s

//~ ERROR this file contains an unclosed delimiter


