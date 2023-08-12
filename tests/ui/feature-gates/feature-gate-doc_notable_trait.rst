tests/ui/feature-gates/feature-gate-doc_notable_trait.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[doc(notable_trait)] //~ ERROR: `#[doc(notable_trait)]` is experimental
trait SomeTrait {}

fn main() {}


