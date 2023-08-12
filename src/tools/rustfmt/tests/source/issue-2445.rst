src/tools/rustfmt/tests/source/issue-2445.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    test!(RunPassPretty {
            // comment
    path: "tests/run-pass/pretty",
    mode: "pretty",
    suite: "run-pass",
    default: false,
    host: true  // should, force, , no trailing comma here
});

test!(RunPassPretty {
            // comment
    path: "tests/run-pass/pretty",
    mode: "pretty",
    suite: "run-pass",
    default: false,
    host: true,         // should, , preserve, the trailing comma
});

test!(Test{
    field: i32, // comment
});


