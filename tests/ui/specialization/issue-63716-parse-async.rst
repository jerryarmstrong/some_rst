tests/ui/specialization/issue-63716-parse-async.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Ensure that `default async fn` will parse.
// See issue #63716 for details.

// check-pass
// edition:2018

#![feature(specialization)] //~ WARN the feature `specialization` is incomplete

fn main() {}

#[cfg(FALSE)]
impl Foo for Bar {
    default async fn baz() {}
}


