tests/ui/feature-gates/soft-syntax-gates-without-errors.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// This file is used to test the behavior of the early-pass syntax warnings.
// If macro syntax is stabilized, replace with a different unstable syntax.

#[cfg(FALSE)]
macro b() {}
//~^ WARN: `macro` is experimental
//~| WARN: unstable syntax

macro_rules! identity {
    ($($x:tt)*) => ($($x)*);
}

#[cfg(FALSE)]
identity! {
    macro d() {} // No error
}

identity! {
    #[cfg(FALSE)]
    macro e() {}
    //~^ WARN: `macro` is experimental
    //~| WARN: unstable syntax
}

fn main() {}


