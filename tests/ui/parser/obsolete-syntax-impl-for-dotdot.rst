tests/ui/parser/obsolete-syntax-impl-for-dotdot.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Trait1 {}
trait Trait2 {}

#[cfg(not_enabled)]
impl Trait1 for .. {}

impl Trait2 for .. {} //~ ERROR `impl Trait for .. {}` is an obsolete syntax

fn main() {}


