src/tools/rustfmt/tests/target/issue-3132.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: Two

fn test() {
    /*
    a
    */
    let x = 42;
    /*
    aaa
    "line 1
  line 2
        line 3"
    */
    let x = 42;
}


