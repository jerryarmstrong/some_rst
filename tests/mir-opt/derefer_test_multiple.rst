tests/mir-opt/derefer_test_multiple.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: Derefer
// EMIT_MIR derefer_test_multiple.main.Derefer.diff
fn main () {
    let mut a = (42, 43);
    let mut b = (99, &mut a);
    let mut c = (11, &mut b);
    let mut d = (13, &mut c);
    let x = &mut (*d.1).1.1.1;
    let y = &mut (*d.1).1.1.1;
}


