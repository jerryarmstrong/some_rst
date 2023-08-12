tests/ui/const-generics/const-parameter-uppercase-lint.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(non_upper_case_globals)]

fn noop<const x: u32>() {
    //~^ ERROR const parameter `x` should have an upper case name
}

fn main() {}


