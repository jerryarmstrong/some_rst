tests/ui/typeof/type_mismatch.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that using typeof results in the correct type mismatch errors instead of always assuming
// `usize`, in addition to the pre-existing "typeof is reserved and unimplemented" error
fn main() {
    const a: u8 = 1;
    let b: typeof(a) = 1i8;
    //~^ ERROR `typeof` is a reserved keyword but unimplemented
    //~| ERROR mismatched types
    //~| expected `u8`, found `i8`
}


