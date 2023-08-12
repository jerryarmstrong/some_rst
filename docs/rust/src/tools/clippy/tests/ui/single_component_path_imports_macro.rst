src/tools/clippy/tests/ui/single_component_path_imports_macro.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::single_component_path_imports)]
#![allow(unused_imports)]

// #7106: use statements exporting a macro within a crate should not trigger lint
// #7923: normal `use` statements of macros should also not trigger the lint

macro_rules! m1 {
    () => {};
}
pub(crate) use m1; // ok

macro_rules! m2 {
    () => {};
}
use m2; // ok

fn main() {
    m1!();
    m2!();
}


