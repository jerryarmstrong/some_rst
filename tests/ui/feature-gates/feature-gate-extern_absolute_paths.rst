tests/ui/feature-gates/feature-gate-extern_absolute_paths.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use core::default; //~ ERROR unresolved import `core`

fn main() {
    let _: u8 = ::core::default::Default(); //~ ERROR failed to resolve
}


