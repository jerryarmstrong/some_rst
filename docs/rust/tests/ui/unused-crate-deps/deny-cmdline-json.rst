tests/ui/unused-crate-deps/deny-cmdline-json.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check for unused crate dep, json event, deny, expect compile failure

// edition:2018
// compile-flags: -Dunused-crate-dependencies  -Zunstable-options --json unused-externs --error-format=json
// aux-crate:bar=bar.rs

fn main() {}


