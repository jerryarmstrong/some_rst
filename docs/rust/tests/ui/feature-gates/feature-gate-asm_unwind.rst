tests/ui/feature-gates/feature-gate-asm_unwind.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-x86_64

use std::arch::asm;

fn main() {
    unsafe {
        asm!("", options(may_unwind));
        //~^ ERROR the `may_unwind` option is unstable
    }
}


