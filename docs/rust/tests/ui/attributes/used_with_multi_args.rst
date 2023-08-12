tests/ui/attributes/used_with_multi_args.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(used_with_arg)]

#[used(compiler, linker)] //~ expected `used`, `used(compiler)` or `used(linker)`
static mut USED_COMPILER_LINKER: [usize; 1] = [0];

fn main() {}


