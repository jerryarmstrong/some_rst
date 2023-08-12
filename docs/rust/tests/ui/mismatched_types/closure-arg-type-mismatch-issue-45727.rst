tests/ui/mismatched_types/closure-arg-type-mismatch-issue-45727.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn main() {
    let _ = (-10..=10).find(|x: i32| x.signum() == 0); //~ ERROR type mismatch in closure arguments
    let _ = (-10..=10).find(|x: &&&i32| x.signum() == 0); //~ ERROR type mismatch in closure arguments
}


