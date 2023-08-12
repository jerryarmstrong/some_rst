src/tools/rustfmt/tests/target/issue-5012/trailing_comma_always.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-trailing_comma: Always

pub struct Matrix<T, const R: usize, const C: usize,>
where
    [T; R * C]:,
{
    contents: [T; R * C],
}


