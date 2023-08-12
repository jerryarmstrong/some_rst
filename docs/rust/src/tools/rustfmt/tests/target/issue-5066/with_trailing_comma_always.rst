src/tools/rustfmt/tests/target/issue-5066/with_trailing_comma_always.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-trailing_comma: Always

fn main() {
    let Foo { a, .. } = b;
}


