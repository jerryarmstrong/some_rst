src/tools/miri/tests/fail/erroneous_const2.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const X: u32 = 5;
const Y: u32 = 6;
const FOO: u32 = [X - Y, Y - X][(X < Y) as usize];
//~^ERROR: evaluation of constant value failed

#[rustfmt::skip] // rustfmt bug: https://github.com/rust-lang/rustfmt/issues/5391
fn main() {
    println!("{}", FOO);
}


