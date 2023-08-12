tests/mir-opt/dest-prop/branch.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Tests that assignment in both branches of an `if` are eliminated.
// unit-test: DestinationPropagation
fn val() -> i32 {
    1
}

fn cond() -> bool {
    true
}

// EMIT_MIR branch.foo.DestinationPropagation.diff
fn foo() -> i32 {
    let x = val();

    let y = if cond() {
        x
    } else {
        val();
        x
    };

    y
}

fn main() {
    foo();
}


