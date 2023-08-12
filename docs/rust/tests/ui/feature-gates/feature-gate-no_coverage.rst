tests/ui/feature-gates/feature-gate-no_coverage.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

#[derive(PartialEq, Eq)] // ensure deriving `Eq` does not enable `feature(no_coverage)`
struct Foo {
    a: u8,
    b: u32,
}

#[no_coverage] //~ ERROR the `#[no_coverage]` attribute is an experimental feature
fn requires_feature_no_coverage() -> bool {
    let bar = Foo { a: 0, b: 0 };
    bar == Foo { a: 0, b: 0 }
}


