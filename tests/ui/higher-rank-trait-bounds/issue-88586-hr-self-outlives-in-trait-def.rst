tests/ui/higher-rank-trait-bounds/issue-88586-hr-self-outlives-in-trait-def.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #88586: a higher-ranked outlives bound on Self in a trait
// definition caused an ICE when debug_assertions were enabled.
//
// Made to pass as part of fixing #98095.
//
// check-pass

trait A where
    for<'a> Self: 'a,
{
}

fn main() {}


