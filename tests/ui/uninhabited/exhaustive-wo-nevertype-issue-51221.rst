tests/ui/uninhabited/exhaustive-wo-nevertype-issue-51221.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(exhaustive_patterns)]

enum Void {}
fn main() {
    let a: Option<Void> = None;
    let None = a;
}


