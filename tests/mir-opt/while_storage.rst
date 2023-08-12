tests/mir-opt/while_storage.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we correctly generate StorageDead statements for while loop
// conditions on all branches

fn get_bool(c: bool) -> bool {
    c
}

// EMIT_MIR while_storage.while_loop.PreCodegen.after.mir
fn while_loop(c: bool) {
    while get_bool(c) {
        if get_bool(c) {
            break;
        }
    }
}

fn main() {
    while_loop(false);
}


