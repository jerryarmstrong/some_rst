tests/ui/impl-trait/universal_multiple_bounds.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::fmt::Display;

fn foo(f: impl Display + Clone) -> String {
    let g = f.clone();
    format!("{} + {}", f, g)
}

fn main() {
    let sum = foo(format!("22"));
    assert_eq!(sum, r"22 + 22");
}


