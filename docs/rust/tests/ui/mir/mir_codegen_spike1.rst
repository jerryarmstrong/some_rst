tests/ui/mir/mir_codegen_spike1.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// A simple spike test for MIR version of codegen.

fn sum(x: i32, y: i32) -> i32 {
    x + y
}

fn main() {
    let x = sum(22, 44);
    assert_eq!(x, 66);
    println!("sum()={:?}", x);
}


