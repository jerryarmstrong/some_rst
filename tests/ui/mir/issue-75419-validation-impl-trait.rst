tests/ui/mir/issue-75419-validation-impl-trait.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass

// This used to fail MIR validation due to the types on both sides of
// an assignment not being equal.
// The failure doesn't occur with a check-only build.

fn iter_slice<'a, T>(xs: &'a [T]) -> impl Iterator<Item = &'a T> {
    xs.iter()
}

fn main() {
    iter_slice::<()> as fn(_) -> _;
}


