tests/ui/mir/mir-inlining/var-debuginfo-issue-67586.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -Z mir-opt-level=3 -C opt-level=0 -C debuginfo=2

#[inline(never)]
pub fn foo(bar: usize) -> usize {
    std::convert::identity(bar)
}

fn main() {
    foo(0);
}


