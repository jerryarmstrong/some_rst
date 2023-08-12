tests/ui/attributes/used_with_arg_no_mangle.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(used_with_arg)]

#[used(linker)]
#[no_mangle] // accidentally detected as `used(compiler)`
pub static GLOB: usize = 0;

fn main() {}


