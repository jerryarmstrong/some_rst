tests/ui/consts/const-eval/transmute-const.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // stderr-per-bitwidth
use std::mem;

static FOO: bool = unsafe { mem::transmute(3u8) };
//~^ ERROR it is undefined behavior to use this value

fn main() {}


