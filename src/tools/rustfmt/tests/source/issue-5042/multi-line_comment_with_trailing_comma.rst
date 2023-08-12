src/tools/rustfmt/tests/source/issue-5042/multi-line_comment_with_trailing_comma.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    // 5042 deals with trailing commas, not the indentation issue of these comments
    // When a future PR fixes the inentation issues these test can be updated
    let _ = std::ops::Add::add(10, 20
        // ...
        // ...,
        );

    let _ = std::ops::Add::add(10, 20
        /* ... */
        // ...,
        );

    let _ = std::ops::Add::add(10, 20
        // ...,
        // ...,
        );

    let _ = std::ops::Add::add(10, 20
        // ...,
        /* ...
        */,
        );
}


