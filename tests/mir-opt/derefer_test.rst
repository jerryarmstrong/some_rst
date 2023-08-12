tests/mir-opt/derefer_test.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: Derefer
// EMIT_MIR derefer_test.main.Derefer.diff
fn main() {
    let mut a = (42,43);
    let mut b = (99, &mut a);
    let x = &mut (*b.1).0;
    let y = &mut (*b.1).1;
}


