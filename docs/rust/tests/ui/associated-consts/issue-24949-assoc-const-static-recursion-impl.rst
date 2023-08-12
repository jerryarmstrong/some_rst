tests/ui/associated-consts/issue-24949-assoc-const-static-recursion-impl.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check for recursion involving references to impl-associated const.

trait Foo {
    const BAR: u32;
}

const IMPL_REF_BAR: u32 = GlobalImplRef::BAR;

struct GlobalImplRef;

impl GlobalImplRef {
    const BAR: u32 = IMPL_REF_BAR; //~ ERROR E0391
}

fn main() {}


