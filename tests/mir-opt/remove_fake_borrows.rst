tests/mir-opt/remove_fake_borrows.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the fake borrows for matches are removed after borrow checking.

// ignore-wasm32-bare compiled with panic=abort by default

// EMIT_MIR remove_fake_borrows.match_guard.CleanupPostBorrowck.diff
fn match_guard(x: Option<&&i32>, c: bool) -> i32 {
    match x {
        Some(0) if c => 0,
        _ => 1,
    }
}

fn main() {
    match_guard(None, true);
}


