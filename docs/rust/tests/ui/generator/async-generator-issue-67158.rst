tests/ui/generator/async-generator-issue-67158.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators)]
// edition:2018
// Regression test for #67158.
fn main() {
    async { yield print!(":C") }; //~ ERROR `async` generators are not yet supported
}


