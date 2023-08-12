tests/ui/rmeta/emit-artifact-notifications.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--emit=metadata --error-format=json --json artifacts
// build-pass
// ignore-pass
// ^-- needed because `--pass check` does not emit the output needed.

// A very basic test for the emission of artifact notifications in JSON output.

fn main() {}


