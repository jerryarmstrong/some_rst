tests/mir-opt/const_goto_storage.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: ConstGoto

// EMIT_MIR const_goto_storage.match_nested_if.ConstGoto.diff
fn match_nested_if() -> bool {
    let val = match () {
        () if if if if true { true } else { false } { true } else { false } {
            true
        } else {
            false
        } =>
            {
                true
            }
        _ => false,
    };
    val
}

fn main() {
    let _ = match_nested_if();
}


