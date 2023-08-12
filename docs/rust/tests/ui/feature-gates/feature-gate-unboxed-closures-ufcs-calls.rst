tests/ui/feature-gates/feature-gate-unboxed-closures-ufcs-calls.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

fn foo<F: Fn()>(mut f: F) {
    Fn::call(&f, ()); //~ ERROR use of unstable library feature 'fn_traits'
    FnMut::call_mut(&mut f, ()); //~ ERROR use of unstable library feature 'fn_traits'
    FnOnce::call_once(f, ()); //~ ERROR use of unstable library feature 'fn_traits'
}

fn main() {}


