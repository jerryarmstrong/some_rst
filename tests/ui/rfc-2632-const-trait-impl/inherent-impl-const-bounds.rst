tests/ui/rfc-2632-const-trait-impl/inherent-impl-const-bounds.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(const_trait_impl)]

struct S;

#[const_trait]
trait A {}
#[const_trait]
trait B {}

impl const A for S {}
impl const B for S {}

impl S {
    const fn a<T: ~const A>() where T: ~const B {

    }
}

const _: () = S::a::<S>();

fn main() {}


