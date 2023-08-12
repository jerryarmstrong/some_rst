tests/ui/regions/issue-72051-member-region-hang.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #72051, hang when resolving regions.

// check-pass
// edition:2018

pub async fn query<'a>(_: &(), _: &(), _: (&(dyn std::any::Any + 'a),) ) {}
fn main() {}


