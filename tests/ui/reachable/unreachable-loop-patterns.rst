tests/ui/reachable/unreachable-loop-patterns.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(never_type, never_type_fallback)]
#![feature(exhaustive_patterns)]

#![allow(unreachable_code)]
#![deny(unreachable_patterns)]

enum Void {}

impl Iterator for Void {
    type Item = Void;

    fn next(&mut self) -> Option<Void> {
        None
    }
}

fn main() {
    for _ in unimplemented!() as Void {}
    //~^ ERROR unreachable pattern
}


