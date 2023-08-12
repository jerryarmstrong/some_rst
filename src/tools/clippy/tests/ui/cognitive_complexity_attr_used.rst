src/tools/clippy/tests/ui/cognitive_complexity_attr_used.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(unused, clippy::cognitive_complexity)]
#![allow(unused_crate_dependencies)]

fn main() {
    kaboom();
}

#[clippy::cognitive_complexity = "0"]
fn kaboom() {
    if 42 == 43 {
        panic!();
    } else if "cake" == "lie" {
        println!("what?");
    }
}


