tests/ui/parser/multiline-comment-line-tracking.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Parse error on line X, but is reported on line Y instead.

/* 1
 * 2
 * 3
 */
fn main() {
  %; //~ ERROR expected expression, found `%`
}


