tests/mir-opt/storage_ranges.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // EMIT_MIR storage_ranges.main.nll.0.mir

fn main() {
    let a = 0;
    {
        let b = &Some(a);
    }
    let c = 1;
}


