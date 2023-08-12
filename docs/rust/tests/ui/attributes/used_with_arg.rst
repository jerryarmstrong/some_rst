tests/ui/attributes/used_with_arg.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(used_with_arg)]

#[used(linker)]
static mut USED_LINKER: [usize; 1] = [0];

#[used(compiler)]
static mut USED_COMPILER: [usize; 1] = [0];

#[used(compiler)] //~ ERROR `used(compiler)` and `used(linker)` can't be used together
#[used(linker)]
static mut USED_COMPILER_LINKER2: [usize; 1] = [0];

#[used(compiler)] //~ ERROR `used(compiler)` and `used(linker)` can't be used together
#[used(linker)]
#[used(compiler)]
#[used(linker)]
static mut USED_COMPILER_LINKER3: [usize; 1] = [0];

fn main() {}


