tests/ui/higher-rank-trait-bounds/hrtb-debruijn-object-types-in-closures.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

trait Typer<'tcx> {
    fn method(&self, data: &'tcx isize) -> &'tcx isize { data }
    fn dummy(&self) { }
}

fn g<F>(_: F) where F: FnOnce(&dyn Typer) {}

fn h() {
    g(|typer| typer.dummy())
}

fn main() { }


