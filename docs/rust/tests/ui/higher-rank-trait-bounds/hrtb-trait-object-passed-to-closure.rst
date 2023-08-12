tests/ui/higher-rank-trait-bounds/hrtb-trait-object-passed-to-closure.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// Test that `&PrinterSupport`, which is really short for `&'a
// PrinterSupport<'b>`, gets properly expanded when it appears in a
// closure type. This used to result in messed up De Bruijn indices.

// pretty-expanded FIXME #23616

trait PrinterSupport<'ast> {
    fn ast_map(&self) -> Option<&'ast usize> { None }
}

struct NoAnn<'ast> {
    f: Option<&'ast usize>
}

impl<'ast> PrinterSupport<'ast> for NoAnn<'ast> {
}

fn foo<'ast, G>(f: Option<&'ast usize>, g: G) where G: FnOnce(&dyn PrinterSupport) {
    let annotation = NoAnn { f: f };
    g(&annotation)
}

fn main() {}


