tests/ui/macros/issue-86082-option-env-invalid-char.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
//
// Regression test for issue #86082
//
// Checks that option_env! does not panic on receiving an invalid
// environment variable name.

fn main() {
    option_env!("\0=");
}


