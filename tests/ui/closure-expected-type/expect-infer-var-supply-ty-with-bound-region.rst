tests/ui/closure-expected-type/expect-infer-var-supply-ty-with-bound-region.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

fn with_closure<F, A>(_: F)
    where F: FnOnce(A, &u32)
{
}

fn foo() {
    // This version works; we infer `A` to be `u32`, and take the type
    // of `y` to be `&u32`.
    with_closure(|x: u32, y| {});
}

fn bar() {
    // This version also works.
    with_closure(|x: &u32, y| {});
}

fn main() { }


