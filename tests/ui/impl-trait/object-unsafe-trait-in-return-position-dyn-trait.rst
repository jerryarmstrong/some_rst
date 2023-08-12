tests/ui/impl-trait/object-unsafe-trait-in-return-position-dyn-trait.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(bare_trait_objects)]
trait NotObjectSafe {
    fn foo() -> Self;
}

struct A;
struct B;

impl NotObjectSafe for A {
    fn foo() -> Self {
        A
    }
}

impl NotObjectSafe for B {
    fn foo() -> Self {
        B
    }
}

fn car() -> dyn NotObjectSafe { //~ ERROR the trait `NotObjectSafe` cannot be made into an object
    if true {
        return A;
    }
    B
}

fn cat() -> Box<dyn NotObjectSafe> { //~ ERROR the trait `NotObjectSafe` cannot be made into an
    if true {
        return Box::new(A);
    }
    Box::new(B)
}

fn main() {}


