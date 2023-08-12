tests/ui/associated-types/associated-types-unconstrained.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that an associated type cannot be bound in an expression path.

trait Foo {
    type A;
    fn bar() -> isize;
}

impl Foo for isize {
    type A = usize;
    fn bar() -> isize { 42 }
}

pub fn main() {
    let x: isize = Foo::bar();
    //~^ ERROR E0790
}


