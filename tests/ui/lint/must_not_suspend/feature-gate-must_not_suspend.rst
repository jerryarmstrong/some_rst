tests/ui/lint/must_not_suspend/feature-gate-must_not_suspend.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

#[must_not_suspend = "You gotta use Umm's, ya know?"] //~ ERROR the `#[must_not_suspend]`
struct Umm {
    _i: i64
}

fn main() {
}


