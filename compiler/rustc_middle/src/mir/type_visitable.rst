compiler/rustc_middle/src/mir/type_visitable.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! `TypeVisitable` implementations for MIR types

use super::*;

impl<'tcx, R: Idx, C: Idx> TypeVisitable<'tcx> for BitMatrix<R, C> {
    fn visit_with<V: TypeVisitor<'tcx>>(&self, _: &mut V) -> ControlFlow<V::BreakTy> {
        ControlFlow::Continue(())
    }
}


