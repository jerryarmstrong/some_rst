tests/ui/dollar-crate/dollar-crate-is-keyword-2.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod a {}

macro_rules! m {
    () => {
        use a::$crate; //~ ERROR unresolved import `a::$crate`
        use a::$crate::b; //~ ERROR `$crate` in paths can only be used in start position
        type A = a::$crate; //~ ERROR `$crate` in paths can only be used in start position
    }
}

m!();

fn main() {}


