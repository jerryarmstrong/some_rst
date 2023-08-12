tests/ui/issues/auxiliary/issue-1920.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Just exporting some type to test for correct diagnostics when this
// crate is pulled in at a non-root location in client crate.

pub struct S;


