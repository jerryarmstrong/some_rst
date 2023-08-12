src/tools/rustfmt/tests/source/configs/indent_style/rfc_where.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-indent_style: Block
// Where style

fn lorem<Ipsum, Dolor, Sit, Amet>() -> T where Ipsum: Eq, Dolor: Eq, Sit: Eq, Amet: Eq {
    // body
}


