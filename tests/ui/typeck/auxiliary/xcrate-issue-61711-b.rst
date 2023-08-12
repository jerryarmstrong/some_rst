tests/ui/typeck/auxiliary/xcrate-issue-61711-b.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
#![crate_type="lib"]
#![crate_name="xcrate_issue_61711_b"]
pub struct Struct;
pub use crate as alias;


