tests/ui/generic-associated-types/variance_constraints.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// issue #69184

trait A {
    type B<'a> where Self: 'a;

    fn make_b<'a>(&'a self) -> Self::B<'a>;
}

struct S {}
impl A for S {
    type B<'a> = &'a S;
    fn make_b<'a>(&'a self) -> &'a Self {
        self
    }
}

enum E<'a> {
    S(<S as A>::B<'a>),
}

fn main() {}


