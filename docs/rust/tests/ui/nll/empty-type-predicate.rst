tests/ui/nll/empty-type-predicate.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #61315
//
// `dyn T:` is lowered to `dyn T: ReEmpty` - check that we don't ICE in NLL for
// the unexpected region.

// check-pass

trait T {}
fn f() where dyn T: {}

fn main() { f(); }


