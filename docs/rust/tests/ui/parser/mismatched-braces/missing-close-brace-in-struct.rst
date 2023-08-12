tests/ui/parser/mismatched-braces/missing-close-brace-in-struct.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub(crate) struct Bar<T> {
  foo: T,

trait T { //~ ERROR expected identifier, found keyword `trait`
    fn foo(&self);
}


impl T for Bar<usize> {
fn foo(&self) {}
}

fn main() {} //~ ERROR this file contains an unclosed delimiter


