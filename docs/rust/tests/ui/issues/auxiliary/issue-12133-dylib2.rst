tests/ui/issues/auxiliary/issue-12133-dylib2.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic

#![crate_type = "dylib"]

extern crate issue_12133_rlib as a;
extern crate issue_12133_dylib as b;


