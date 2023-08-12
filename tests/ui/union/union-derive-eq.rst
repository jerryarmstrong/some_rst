tests/ui/union/union-derive-eq.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mirunsafeck thirunsafeck
// [thirunsafeck]compile-flags: -Z thir-unsafeck

#[derive(Eq)] // OK
union U1 {
    a: u8,
}

impl PartialEq for U1 { fn eq(&self, rhs: &Self) -> bool { true } }

#[derive(PartialEq, Copy, Clone)]
struct PartialEqNotEq;

#[derive(Eq)]
union U2 {
    a: PartialEqNotEq, //~ ERROR the trait bound `PartialEqNotEq: Eq` is not satisfied
}

impl PartialEq for U2 { fn eq(&self, rhs: &Self) -> bool { true } }

fn main() {}


