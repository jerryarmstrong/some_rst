tests/ui/modules/mod-view-items.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test view items inside non-file-level mods

// This is a regression test for an issue where we were failing to
// pretty-print such view items. If that happens again, this should
// begin failing.

// pretty-expanded FIXME #23616

mod m {
    pub fn f() -> Vec<isize> { Vec::new() }
}

pub fn main() { let _x = m::f(); }


