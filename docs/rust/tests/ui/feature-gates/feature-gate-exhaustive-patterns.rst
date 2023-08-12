tests/ui/feature-gates/feature-gate-exhaustive-patterns.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(never_type)]

fn foo() -> Result<u32, !> {
    Ok(123)
}

fn main() {
    let Ok(_x) = foo(); //~ ERROR refutable pattern in local binding
}


