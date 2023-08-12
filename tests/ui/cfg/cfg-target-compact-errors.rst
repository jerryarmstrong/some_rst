tests/ui/cfg/cfg-target-compact-errors.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

#![feature(cfg_target_compact)]

#[cfg(target(o::o))]
//~^ ERROR `cfg` predicate key must be an identifier
fn one() {}

#[cfg(target(os = 8))]
//~^ ERROR literal in `cfg` predicate value must be a string
fn two() {}

#[cfg(target(os = "linux", pointer(width = "64")))]
//~^ ERROR invalid predicate `target_pointer`
fn three() {}

fn main() {}


