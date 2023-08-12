tests/ui/consts/promoted_regression.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

fn main() {
    let _ = &[("", ""); 3];
}

const FOO: &[(&str, &str)] = &[("", ""); 3];
const BAR: &[(&str, &str); 5] = &[("", ""); 5];
const BAA: &[[&str; 12]; 11] = &[[""; 12]; 11];


