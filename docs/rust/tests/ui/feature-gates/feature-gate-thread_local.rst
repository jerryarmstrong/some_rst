tests/ui/feature-gates/feature-gate-thread_local.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that `#[thread_local]` attribute is gated by `thread_local`
// feature gate.
//
// (Note that the `thread_local!` macro is explicitly *not* gated; it
// is given permission to expand into this unstable attribute even
// when the surrounding context does not have permission to use it.)

#[thread_local] //~ ERROR `#[thread_local]` is an experimental feature
static FOO: i32 = 3;

pub fn main() {}


