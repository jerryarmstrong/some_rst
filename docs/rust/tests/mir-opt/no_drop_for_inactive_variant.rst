tests/mir-opt/no_drop_for_inactive_variant.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-wasm32-bare compiled with panic=abort by default

// Ensure that there are no drop terminators in `unwrap<T>` (except the one along the cleanup
// path).

// EMIT_MIR no_drop_for_inactive_variant.unwrap.SimplifyCfg-elaborate-drops.after.mir
fn unwrap<T>(opt: Option<T>) -> T {
    match opt {
        Some(x) => x,
        None => panic!(),
    }
}

fn main() {
    let _ = unwrap(Some(1i32));
}


