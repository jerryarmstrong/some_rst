tests/ui/generator/reinit-in-match-guard.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass

#![feature(generators)]

#![allow(unused_assignments, dead_code)]

fn main() {
    let _ = || {
        let mut x = vec![22_usize];
        std::mem::drop(x);
        match y() {
            true if {
                x = vec![];
                false
            } => {}
            _ => {
                yield;
            }
        }
    };
}

fn y() -> bool {
    true
}


