tests/codegen/issue-45964-bounds-check-slice-pos.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test case checks that slice::{r}position functions do not
// prevent optimizing away bounds checks

// compile-flags: -O
// ignore-debug: the debug assertions get in the way

#![crate_type="rlib"]

// CHECK-LABEL: @test
#[no_mangle]
pub fn test(y: &[u32], x: &u32, z: &u32) -> bool {
    let result = match y.iter().position(|a| a == x) {
        Some(p) => Ok(p),
        None => Err(()),
    };

    if let Ok(p) = result {
        // CHECK-NOT: panic
        y[p] == *z
    } else {
        false
    }
}

// CHECK-LABEL: @rtest
#[no_mangle]
pub fn rtest(y: &[u32], x: &u32, z: &u32) -> bool {
    let result = match y.iter().rposition(|a| a == x) {
        Some(p) => Ok(p),
        None => Err(()),
    };

    if let Ok(p) = result {
        // CHECK-NOT: panic
        y[p] == *z
    } else {
        false
    }
}


