compiler/rustc_codegen_ssa/src/traits/abi.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::BackendTypes;

pub trait AbiBuilderMethods<'tcx>: BackendTypes {
    fn get_param(&mut self, index: usize) -> Self::Value;
}


