tests/ui/async-await/async-trait-fn.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
trait T {
    async fn foo() {} //~ ERROR functions in traits cannot be declared `async`
    async fn bar(&self) {} //~ ERROR functions in traits cannot be declared `async`
    async fn baz() { //~ ERROR functions in traits cannot be declared `async`
        // Nested item must not ICE.
        fn a() {}
    }
}

fn main() {}


