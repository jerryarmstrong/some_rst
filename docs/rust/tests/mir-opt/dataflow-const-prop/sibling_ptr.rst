tests/mir-opt/dataflow-const-prop/sibling_ptr.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: DataflowConstProp

// EMIT_MIR sibling_ptr.main.DataflowConstProp.diff
fn main() {
    let mut x: (u8, u8) = (0, 0);
    unsafe {
        let p = std::ptr::addr_of_mut!(x.0);
        *p.add(1) = 1;
    }
    let x1 = x.1;  // should not be propagated
}


