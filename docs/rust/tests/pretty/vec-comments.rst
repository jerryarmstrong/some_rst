tests/pretty/vec-comments.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue #679
// Testing that comments are correctly interleaved
// pp-exact:vec-comments.pp
fn main() {
    let _v1 =
        [
         // Comment
         0,
         // Comment
         1,
         // Comment
         2];
    let _v2 =
        [0, // Comment
         1, // Comment
         2]; // Comment
    let _v3 =
        [
         /* Comment */
         0,
         /* Comment */
         1,
         /* Comment */
         2];
    let _v4 =
        [0, /* Comment */
         1, /* Comment */
         2]; /* Comment */
}


