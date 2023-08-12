tests/ui/macros/global-asm.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::arch::global_asm;

fn main() {
    global_asm!(); //~ ERROR requires at least a template string argument
    global_asm!(struct); //~ ERROR expected expression
    global_asm!(123); //~ ERROR asm template must be a string literal
}


