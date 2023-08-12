tests/ui/feature-gates/feature-gate-linkage.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    #[linkage = "extern_weak"] static foo: *mut isize;
    //~^ ERROR: the `linkage` attribute is experimental and not portable
}

fn main() {}


