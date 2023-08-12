tests/ui/lint/command-line-lint-group-allow.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -A bad-style
// check-pass

fn main() {
    let _InappropriateCamelCasing = true;
}


