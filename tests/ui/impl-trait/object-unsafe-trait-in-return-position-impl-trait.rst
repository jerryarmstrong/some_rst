tests/ui/impl-trait/object-unsafe-trait-in-return-position-impl-trait.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait NotObjectSafe {
    fn foo() -> Self;
}

trait ObjectSafe {
    fn bar(&self);
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

impl ObjectSafe for A {
    fn bar(&self) {}
}

impl ObjectSafe for B {
    fn bar(&self) {}
}

fn can() -> impl NotObjectSafe {
    if true {
        return A;
    }
    B //~ ERROR mismatched types
}

fn cat() -> impl ObjectSafe {
    if true {
        return A;
    }
    B //~ ERROR mismatched types
}

fn main() {}


