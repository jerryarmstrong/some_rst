tests/ui/rfc-0107-bind-by-move-pattern-guards/former-E0008-now-pass.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test used to emit E0008 but now passed since `bind_by_move_pattern_guards`
// have been stabilized.

// check-pass

fn main() {
    match Some("hi".to_string()) {
        Some(s) if s.len() == 0 => {},
        _ => {},
    }
}


