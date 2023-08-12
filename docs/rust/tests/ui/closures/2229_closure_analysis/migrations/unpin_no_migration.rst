tests/ui/closures/2229_closure_analysis/migrations/unpin_no_migration.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //run-pass
#![deny(rust_2021_incompatible_closure_captures)]
#![allow(unused_must_use)]

fn filter_try_fold(
    predicate: &mut impl FnMut() -> bool,
) -> impl FnMut() -> bool + '_ {
    move || predicate()
}

fn main() {
    filter_try_fold(&mut || true);
}


