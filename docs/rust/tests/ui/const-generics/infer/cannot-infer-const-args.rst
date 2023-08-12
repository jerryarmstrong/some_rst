tests/ui/const-generics/infer/cannot-infer-const-args.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<const X: usize>() -> usize {
    0
}

fn main() {
    foo(); //~ ERROR type annotations needed
}


