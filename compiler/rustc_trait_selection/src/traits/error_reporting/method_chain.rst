compiler/rustc_trait_selection/src/traits/error_reporting/method_chain.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::infer::InferCtxt;

use rustc_middle::ty::error::TypeError;
use rustc_middle::ty::relate::{self, Relate, RelateResult, TypeRelation};
use rustc_middle::ty::{self, Ty, TyCtxt};

pub struct CollectAllMismatches<'a, 'tcx> {
    pub infcx: &'a InferCtxt<'tcx>,
    pub param_env: ty::ParamEnv<'tcx>,
    pub errors: Vec<TypeError<'tcx>>,
}

impl<'a, 'tcx> TypeRelation<'tcx> for CollectAllMismatches<'a, 'tcx> {
    fn tag(&self) -> &'static str {
        "CollectAllMismatches"
    }

    fn tcx(&self) -> TyCtxt<'tcx> {
        self.infcx.tcx
    }

    fn intercrate(&self) -> bool {
        false
    }

    fn param_env(&self) -> ty::ParamEnv<'tcx> {
        self.param_env
    }

    fn a_is_expected(&self) -> bool {
        true
    }

    fn mark_ambiguous(&mut self) {
        bug!()
    }

    fn relate_with_variance<T: Relate<'tcx>>(
        &mut self,
        _: ty::Variance,
        _: ty::VarianceDiagInfo<'tcx>,
        a: T,
        b: T,
    ) -> RelateResult<'tcx, T> {
        self.relate(a, b)
    }

    fn regions(
        &mut self,
        a: ty::Region<'tcx>,
        _b: ty::Region<'tcx>,
    ) -> RelateResult<'tcx, ty::Region<'tcx>> {
        Ok(a)
    }

    fn tys(&mut self, a: Ty<'tcx>, b: Ty<'tcx>) -> RelateResult<'tcx, Ty<'tcx>> {
        self.infcx.probe(|_| {
            if a.is_ty_var() || b.is_ty_var() {
                Ok(a)
            } else {
                self.infcx.super_combine_tys(self, a, b).or_else(|e| {
                    self.errors.push(e);
                    Ok(a)
                })
            }
        })
    }

    fn consts(
        &mut self,
        a: ty::Const<'tcx>,
        b: ty::Const<'tcx>,
    ) -> RelateResult<'tcx, ty::Const<'tcx>> {
        self.infcx.probe(|_| {
            if a.is_ct_infer() || b.is_ct_infer() {
                Ok(a)
            } else {
                relate::super_relate_consts(self, a, b) // could do something similar here for constants!
            }
        })
    }

    fn binders<T: Relate<'tcx>>(
        &mut self,
        a: ty::Binder<'tcx, T>,
        b: ty::Binder<'tcx, T>,
    ) -> RelateResult<'tcx, ty::Binder<'tcx, T>> {
        Ok(a.rebind(self.relate(a.skip_binder(), b.skip_binder())?))
    }
}


