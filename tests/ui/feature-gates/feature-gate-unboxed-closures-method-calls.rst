tests/ui/feature-gates/feature-gate-unboxed-closures-method-calls.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

fn foo<F: Fn()>(mut f: F) {
    f.call(()); //~ ERROR use of unstable library feature 'fn_traits'
    f.call_mut(()); //~ ERROR use of unstable library feature 'fn_traits'
    f.call_once(()); //~ ERROR use of unstable library feature 'fn_traits'
}

fn main() {}


