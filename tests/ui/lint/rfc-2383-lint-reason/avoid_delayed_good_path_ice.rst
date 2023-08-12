tests/ui/lint/rfc-2383-lint-reason/avoid_delayed_good_path_ice.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(lint_reasons)]

#[expect(drop_bounds)]
fn trigger_rustc_lints<T: Drop>() {
}

fn main() {}


