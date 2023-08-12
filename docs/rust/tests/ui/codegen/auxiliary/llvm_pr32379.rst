tests/ui/codegen/auxiliary/llvm_pr32379.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn pr32379(mut data: u64, f1: bool, f2: bool) -> u64 {
    if f1 { data &= !2; }
    if f2 { data |= 2; }
    data
}


