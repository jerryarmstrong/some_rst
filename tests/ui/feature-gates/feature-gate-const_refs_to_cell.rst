tests/ui/feature-gates/feature-gate-const_refs_to_cell.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(const_refs_to_cell)]

const FOO: () = {
    let x = std::cell::Cell::new(42);
    let y = &x;
};

fn main() {
    FOO;
}


