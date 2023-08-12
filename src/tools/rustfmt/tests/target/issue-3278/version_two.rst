src/tools/rustfmt/tests/target/issue-3278/version_two.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: Two

pub fn parse_conditional<'a, I: 'a>()
-> impl Parser<Input = I, Output = Expr, PartialState = ()> + 'a
where
    I: Stream<Item = char>,
{
}


