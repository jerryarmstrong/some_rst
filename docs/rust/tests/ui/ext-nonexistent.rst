tests/ui/ext-nonexistent.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:cannot find macro
fn main() { iamnotanextensionthatexists!(""); }


