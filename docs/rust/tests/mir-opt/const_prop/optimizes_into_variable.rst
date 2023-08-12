tests/mir-opt/const_prop/optimizes_into_variable.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test
// compile-flags: -C overflow-checks=on

struct Point {
    x: u32,
    y: u32,
}

// EMIT_MIR_FOR_EACH_BIT_WIDTH
// EMIT_MIR optimizes_into_variable.main.ScalarReplacementOfAggregates.diff
// EMIT_MIR optimizes_into_variable.main.ConstProp.diff
// EMIT_MIR optimizes_into_variable.main.SimplifyLocals-final.after.mir
// EMIT_MIR optimizes_into_variable.main.PreCodegen.after.mir
fn main() {
    let x = 2 + 2;
    let y = [0, 1, 2, 3, 4, 5][3];
    let z = (Point { x: 12, y: 42}).y;
}


