tests/incremental/issue-39828/auxiliary/generic.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions:rpass1 rpass2
// compile-flags: -Z query-dep-graph

#![rustc_partition_reused(module="generic-fallback.cgu", cfg="rpass2")]
#![feature(rustc_attrs)]

#![crate_type="rlib"]
pub fn foo<T>() { }


