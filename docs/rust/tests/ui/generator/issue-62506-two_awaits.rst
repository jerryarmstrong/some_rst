tests/ui/generator/issue-62506-two_awaits.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Output = String caused an ICE whereas Output = &'static str compiled successfully.
// Broken MIR: generator contains type std::string::String in MIR,
// but typeck only knows about {<S as T>::Future, ()}
// check-pass
// edition:2018

use std::future::Future;

pub trait T {
    type Future: Future<Output = String>;
    fn bar() -> Self::Future;
}
pub async fn foo<S>() where S: T {
    S::bar().await;
    S::bar().await;
}
pub fn main() {}


