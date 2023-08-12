tests/ui/lint/lint-removed.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // The raw_pointer_derived lint was removed, but is now reported by
// the renamed_and_removed_lints lint, which means it's a warning by
// default, and allowed in cargo dependency builds.
// cc #30346

#[deny(raw_pointer_derive)] //~ WARN `raw_pointer_derive` has been removed
#[deny(unused_variables)]
fn main() { let unused = (); } //~ ERROR unused


