tests/ui/match/const_non_normal_zst_ref_pattern.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

const FOO: isize = 10;
const ZST: &() = unsafe { std::mem::transmute(FOO) };
fn main() {
    match &() {
        ZST => 9,
    };
}


