tests/ui/suggestions/suggest-imm-mut-trait-implementations.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Trait {}

struct A;
struct B;
struct C;

impl Trait for &A {}
impl Trait for &mut A {}

impl Trait for &B {}

impl Trait for &mut C {}

fn foo<X: Trait>(_: X) {}

fn main() {
    let a = A;
    let b = B;
    let c = C;
    foo(a); //~ ERROR the trait bound `A: Trait` is not satisfied
    foo(b); //~ ERROR the trait bound `B: Trait` is not satisfied
    foo(c); //~ ERROR the trait bound `C: Trait` is not satisfied
}


