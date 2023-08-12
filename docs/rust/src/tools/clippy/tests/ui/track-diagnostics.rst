src/tools/clippy/tests/ui/track-diagnostics.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z track-diagnostics
// error-pattern: created at

// Normalize the emitted location so this doesn't need
// updating everytime someone adds or removes a line.
// normalize-stderr-test ".rs:\d+:\d+" -> ".rs:LL:CC"

struct A;
struct B;
const S: A = B;

fn main() {}


