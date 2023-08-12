tests/ui/feature-gates/feature-gate-repr-simd.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[repr(simd)] //~ error: SIMD types are experimental
struct Foo(u64, u64);

#[repr(C)] //~ ERROR conflicting representation hints
//~^ WARN this was previously accepted
#[repr(simd)] //~ error: SIMD types are experimental
struct Bar(u64, u64);

fn main() {}


