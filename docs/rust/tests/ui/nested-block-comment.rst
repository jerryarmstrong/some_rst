tests/ui/nested-block-comment.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

/* This test checks that nested comments are supported

   /*
     This should not panic
   */
*/

pub fn main() {
}


