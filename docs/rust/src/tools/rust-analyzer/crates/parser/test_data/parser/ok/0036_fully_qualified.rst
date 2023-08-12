src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0036_fully_qualified.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // https://github.com/rust-lang/rust-analyzer/issues/311

pub fn foo<S: Iterator>() -> String
where
    <S as Iterator>::Item: Eq,
{
    "".to_owned()
}


