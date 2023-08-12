tests/ui/consts/const-eval/ice-packed.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #50356: Compiler panic when using repr(packed)
// associated constant in a match arm

// check-pass
#[derive(Copy, Clone, PartialEq, Eq)]
#[repr(packed)]
pub struct Num(u64);

impl Num {
    pub const ZERO: Self = Num(0);
}

pub fn decrement(a: Num) -> Num {
    match a {
        Num::ZERO => Num::ZERO,
        a => Num(a.0 - 1)
    }
}

fn main() {
}


