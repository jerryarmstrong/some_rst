tests/ui/issues/issue-1362.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #1362 - without that fix the span will be bogus
// no-reformat
fn main() {
  let x: u32 = 20i32; //~ ERROR mismatched types
}
// NOTE: Do not add any extra lines as the line number the error is
// on is significant; an error later in the source file might not
// trigger the bug.


