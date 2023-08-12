tests/ui/unused-crate-deps/deny-cmdline-json-silent.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check for unused crate dep, json event, deny but we're not reporting that in exit status

// edition:2018
// check-pass
// compile-flags: -Dunused-crate-dependencies -Zunstable-options --json unused-externs-silent --error-format=json
// aux-crate:bar=bar.rs

fn main() {}


