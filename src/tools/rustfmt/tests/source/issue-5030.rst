src/tools/rustfmt/tests/source/issue-5030.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-imports_granularity: Item
// rustfmt-group_imports: One

// Confirm that attributes are duplicated to all items in the use statement
#[cfg(feature = "foo")]
use std::collections::{
    HashMap,
    HashSet,
};

// Separate the imports below from the ones above
const A: usize = 0;

// Copying attrs works with import grouping as well
#[cfg(feature = "foo")]
use std::collections::{
    HashMap,
    HashSet,
};

#[cfg(feature = "spam")]
use qux::{bar, baz};


