tests/ui/typeck/auxiliary/issue-81943-lib.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn g(t: i32) -> i32 { t }
// This function imitates `dbg!` so that future changes
// to its macro definition won't make this test a dud.
#[macro_export]
macro_rules! d {
  ($e:expr) => { match $e { x => { $crate::g(x) } } }
}


