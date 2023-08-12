src/tools/rustfmt/tests/source/issue-5042/single-line_comment_without_trailing_comma.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = std::ops::Add::add(10, 20
        // ...
        );

    let _ = std::ops::Add::add(10, 20
        /* ... */
        );
}



