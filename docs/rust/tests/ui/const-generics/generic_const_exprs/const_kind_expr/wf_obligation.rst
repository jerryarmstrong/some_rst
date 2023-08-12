tests/ui/const-generics/generic_const_exprs/const_kind_expr/wf_obligation.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs, generic_arg_infer)]
#![allow(incomplete_features)]

// minimized repro for #105205
//
// the `foo::<_, L>` call results in a `WellFormed(_)` obligation and a
// `ConstEvaluatable(Unevaluated(_ + 1 + L))` obligation. Attempting to fulfill the latter
// unifies the `_` with `Expr(L - 1)` from the paramenv which turns the `WellFormed`
// obligation into `WellFormed(Expr(L - 1))`

fn foo<const N: usize, const M: usize>(_: [(); N + 1 + M]) {}

fn ice<const L: usize>()
where
    [(); (L - 1) + 1 + L]:,
{
    foo::<_, L>([(); L + 1 + L]);
    //~^ ERROR: mismatched types
    //~^^ ERROR: unconstrained generic constant
}

fn main() {}


