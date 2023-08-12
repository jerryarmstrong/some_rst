tests/ui/codegen/issue-82859-slice-miscompile.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -Copt-level=0 -Cdebuginfo=2

// Make sure LLVM does not miscompile this.

fn indirect_get_slice() -> &'static [usize] {
    &[]
}

#[inline(always)]
fn get_slice() -> &'static [usize] {
    let ret = indirect_get_slice();
    ret
}

fn main() {
    let output = get_slice().len();
    assert_eq!(output, 0);
}


