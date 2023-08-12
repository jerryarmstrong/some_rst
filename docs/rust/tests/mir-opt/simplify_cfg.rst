tests/mir-opt/simplify_cfg.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the goto chain starting from bb0 is collapsed.
// compile-flags: -Cpanic=abort
// no-prefer-dynamic

// EMIT_MIR simplify_cfg.main.SimplifyCfg-initial.diff
// EMIT_MIR simplify_cfg.main.SimplifyCfg-early-opt.diff
fn main() {
    loop {
        if bar() {
            break;
        }
    }
}

#[inline(never)]
fn bar() -> bool {
    true
}


