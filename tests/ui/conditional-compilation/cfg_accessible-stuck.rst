tests/ui/conditional-compilation/cfg_accessible-stuck.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(cfg_accessible)]

#[cfg_accessible(Z)] // OK, recovered after the other `cfg_accessible` produces an error.
struct S;

#[cfg_accessible(S)] //~ ERROR cannot determine whether the path is accessible or not
struct Z;

fn main() {}


