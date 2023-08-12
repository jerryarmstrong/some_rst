tests/ui/async-await/feature-async-closure.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// gate-test-async_closure

fn f() {
    let _ = async || {}; //~ ERROR async closures are unstable
}

fn main() {}


