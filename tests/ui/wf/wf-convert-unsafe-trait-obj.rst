tests/ui/wf/wf-convert-unsafe-trait-obj.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we do not allow casts or coercions
// to object unsafe trait objects by ref

#![feature(object_safe_for_dispatch)]

trait Trait: Sized {}

struct S;

impl Trait for S {}

fn takes_trait(t: &dyn Trait) {}

fn main() {
    &S as &dyn Trait; //~ ERROR E0038
    let t: &dyn Trait = &S; //~ ERROR E0038
    takes_trait(&S); //~ ERROR E0038
}


