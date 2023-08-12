src/tools/rustfmt/tests/target/issue-5030.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-imports_granularity: Item
// rustfmt-group_imports: One

// Confirm that attributes are duplicated to all items in the use statement
#[cfg(feature = "foo")]
use std::collections::HashMap;
#[cfg(feature = "foo")]
use std::collections::HashSet;

// Separate the imports below from the ones above
const A: usize = 0;

// Copying attrs works with import grouping as well
#[cfg(feature = "spam")]
use qux::bar;
#[cfg(feature = "spam")]
use qux::baz;
#[cfg(feature = "foo")]
use std::collections::HashMap;
#[cfg(feature = "foo")]
use std::collections::HashSet;


