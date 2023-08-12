tests/ui/regions/regions-debruijn-of-object.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(non_camel_case_types)]

// pretty-expanded FIXME #23616

struct ctxt<'tcx> {
    x: &'tcx i32
}

trait AstConv<'tcx> {
    fn tcx<'a>(&'a self) -> &'a ctxt<'tcx>;
}

fn foo(conv: &dyn AstConv) { }

fn bar<'tcx>(conv: &dyn AstConv<'tcx>) {
    foo(conv)
}

fn main() { }


