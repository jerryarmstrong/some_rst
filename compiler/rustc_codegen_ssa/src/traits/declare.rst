compiler/rustc_codegen_ssa/src/traits/declare.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::BackendTypes;
use rustc_hir::def_id::DefId;
use rustc_middle::mir::mono::{Linkage, Visibility};
use rustc_middle::ty::Instance;

pub trait PreDefineMethods<'tcx>: BackendTypes {
    fn predefine_static(
        &self,
        def_id: DefId,
        linkage: Linkage,
        visibility: Visibility,
        symbol_name: &str,
    );
    fn predefine_fn(
        &self,
        instance: Instance<'tcx>,
        linkage: Linkage,
        visibility: Visibility,
        symbol_name: &str,
    );
}


