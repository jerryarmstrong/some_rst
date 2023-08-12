tests/ui/type/type-check/unknown_type_for_closure.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn infer_in_arg() {
    let x = |b: Vec<_>| {}; //~ ERROR E0282
}

fn empty_pattern() {
    let x = |_| {}; //~ ERROR type annotations needed
}

fn infer_ty() {
    let x = |k: _| {}; //~ ERROR type annotations needed
}

fn ambig_return() {
    let x = || -> Vec<_> { Vec::new() }; //~ ERROR type annotations needed
}

fn main() {}


