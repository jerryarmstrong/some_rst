tests/ui/wf/wf-unsafe-trait-obj-match.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we do not allow coercions to object
// unsafe trait objects in match arms

#![feature(object_safe_for_dispatch)]

trait Trait: Sized {}

struct S;

impl Trait for S {}

struct R;

impl Trait for R {}

fn opt() -> Option<()> {
    Some(())
}

fn main() {
    match opt() {
        Some(()) => &S,
        None => &R,  //~ ERROR E0308
    }
    let t: &dyn Trait = match opt() { //~ ERROR E0038
        Some(()) => &S, //~ ERROR E0038
        None => &R,
    };
}


