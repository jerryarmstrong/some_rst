tests/ui/closures/2229_closure_analysis/match/auxiliary/match_non_exhaustive_lib.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[non_exhaustive]
pub enum E1 {}

#[non_exhaustive]
pub enum E2 { A, B }

#[non_exhaustive]
pub enum E3 { C }

pub enum E4 { D }


