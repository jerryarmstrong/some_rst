src/tools/rustfmt/tests/target/issue-5033/nested_modules.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![rustfmt::skip]

mod a {
    mod b {

    }

    // trailing comment b
}

// trailing comment a


