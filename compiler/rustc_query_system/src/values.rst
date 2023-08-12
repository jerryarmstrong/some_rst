compiler/rustc_query_system/src/values.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::dep_graph::{DepContext, DepKind};
use crate::query::QueryInfo;

pub trait Value<Tcx: DepContext, D: DepKind>: Sized {
    fn from_cycle_error(tcx: Tcx, cycle: &[QueryInfo<D>]) -> Self;
}

impl<Tcx: DepContext, T, D: DepKind> Value<Tcx, D> for T {
    default fn from_cycle_error(tcx: Tcx, _: &[QueryInfo<D>]) -> T {
        tcx.sess().abort_if_errors();
        // Ideally we would use `bug!` here. But bug! is only defined in rustc_middle, and it's
        // non-trivial to define it earlier.
        panic!("Value::from_cycle_error called without errors");
    }
}


