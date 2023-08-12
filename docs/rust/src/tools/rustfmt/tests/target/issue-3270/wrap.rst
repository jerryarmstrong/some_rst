src/tools/rustfmt/tests/target/issue-3270/wrap.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-wrap_comments: true
// rustfmt-version: Two

// check that a line below max_width does not get over the limit when wrapping
// it in a block comment
fn func() {
    let x = 42;
    /*
    let something = "one line line  line  line  line  line  line  line  line  line  line  line line
  two lines
         three lines";
     */
}


