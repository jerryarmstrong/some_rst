tests/ui/hygiene/macro-metavars-transparent.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Ensure macro metavariables are not compared without removing transparent
// marks.

#![feature(rustc_attrs)]

// run-pass

#[rustc_macro_transparency = "transparent"]
macro_rules! k {
    ($($s:tt)*) => {
        macro_rules! m {
            ($y:tt) => {
                $($s)*
            }
        }
    }
}

k!(1 + $y);

fn main() {
    let x = 2;
    assert_eq!(3, m!(x));
}


