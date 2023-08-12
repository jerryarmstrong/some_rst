tests/ui/async-await/issue-75785-confusing-named-region.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
//
// Regression test for issue #75785
// Tests that we don't point to a confusing named
// region when emitting a diagnostic

pub async fn async_fn(x: &mut i32) -> (&i32, &i32) {
    let y = &*x;
    *x += 1; //~ ERROR cannot assign to
    (&32, y)
}

fn main() {}


