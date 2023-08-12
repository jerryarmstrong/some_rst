tests/ui/const-generics/defaults/simple-defaults.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Checks that type param defaults are allowed after const params.
#![allow(dead_code)]

struct FixedOutput<'a, const N: usize, T=u32> {
    out: &'a [T; N],
}

trait FixedOutputter {
    fn out(&self) -> FixedOutput<'_, 10>;
}

fn main() {}


