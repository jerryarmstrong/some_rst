tests/ui/typeck/assign-non-lval-needs-deref.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // issue #101376

use std::ops::AddAssign;
struct Foo;

impl AddAssign<()> for Foo {
    fn add_assign(&mut self, _: ()) {}
}

impl AddAssign<()> for &mut Foo {
    fn add_assign(&mut self, _: ()) {}
}

fn main() {
    (&mut Foo) += ();
    //~^ ERROR invalid left-hand side of assignment
    //~| NOTE cannot assign to this expression
    //~| HELP consider dereferencing the left-hand side of this operation
}


