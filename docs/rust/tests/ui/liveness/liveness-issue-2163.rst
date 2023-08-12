tests/ui/liveness/liveness-issue-2163.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::vec::Vec;

fn main() {
    let a: Vec<isize> = Vec::new();
    a.iter().all(|_| -> bool {
        //~^ ERROR mismatched types
    });
}


