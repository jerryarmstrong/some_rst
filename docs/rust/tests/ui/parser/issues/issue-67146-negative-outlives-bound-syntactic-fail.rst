tests/ui/parser/issues/issue-67146-negative-outlives-bound-syntactic-fail.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

// In this regression test for #67146, we check that the
// negative outlives bound `!'a` is rejected by the parser.
// This regression was first introduced in PR #57364.

fn main() {}

pub fn f1<T: !'static>() {}
//~^ ERROR negative bounds are not supported
pub fn f2<'a, T: Ord + !'a>() {}
//~^ ERROR negative bounds are not supported
pub fn f3<'a, T: !'a + Ord>() {}
//~^ ERROR negative bounds are not supported


