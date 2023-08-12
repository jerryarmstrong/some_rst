tests/ui/array-slice-vec/dst-raw-slice.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test bounds checking for DST raw slices

// run-fail
// error-pattern:index out of bounds
// ignore-emscripten no processes

#[allow(unconditional_panic)]
fn main() {
    let a: *const [_] = &[1, 2, 3];
    unsafe {
        let _b = (*a)[3];
    }
}


