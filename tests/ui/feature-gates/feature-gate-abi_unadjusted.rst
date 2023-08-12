tests/ui/feature-gates/feature-gate-abi_unadjusted.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "unadjusted" fn foo() {
//~^ ERROR: unadjusted ABI is an implementation detail and perma-unstable
}

fn main() {
    foo();
}


