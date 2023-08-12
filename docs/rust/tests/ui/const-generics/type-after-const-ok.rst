tests/ui/const-generics/type-after-const-ok.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Verifies that having generic parameters after constants is permitted
#[allow(dead_code)]
struct A<const N: usize, T>(T);

fn main() {}


