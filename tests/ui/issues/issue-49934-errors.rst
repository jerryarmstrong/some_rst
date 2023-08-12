tests/ui/issues/issue-49934-errors.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<#[derive(Debug)] T>() { //~ ERROR expected non-macro attribute, found attribute macro
    match 0 {
        #[derive(Debug)] //~ ERROR expected non-macro attribute, found attribute macro
        _ => (),
    }
}

fn main() {}


