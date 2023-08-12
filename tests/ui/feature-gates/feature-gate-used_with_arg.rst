tests/ui/feature-gates/feature-gate-used_with_arg.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[used(linker)] //~ ERROR `#[used(linker)]` is currently unstable
static mut USED_LINKER: [usize; 1] = [0];

#[used(compiler)] //~ ERROR `#[used(compiler)]` is currently unstable
static mut USED_COMPILER: [usize; 1] = [0];

fn main() {}


