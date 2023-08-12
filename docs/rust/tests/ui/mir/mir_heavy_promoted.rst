tests/ui/mir/mir_heavy_promoted.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-emscripten apparently only works in optimized mode

const TEST_DATA: [u8; 32 * 1024 * 1024] = [42; 32 * 1024 * 1024];

// Check that the promoted copy of TEST_DATA doesn't
// leave an alloca from an unused temp behind, which,
// without optimizations, can still blow the stack.
fn main() {
    println!("{}", TEST_DATA.len());
}


