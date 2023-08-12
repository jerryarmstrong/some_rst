tests/ui/wf/wf-convert-unsafe-trait-obj-box.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we do not allow casts or coercions
// to object unsafe trait objects inside a Box

#![feature(object_safe_for_dispatch)]

trait Trait: Sized {}

struct S;

impl Trait for S {}

fn takes_box(t: Box<dyn Trait>) {}

fn main() {
    Box::new(S) as Box<dyn Trait>; //~ ERROR E0038
    let t_box: Box<dyn Trait> = Box::new(S); //~ ERROR E0038
    takes_box(Box::new(S)); //~ ERROR E0038
}


