src/tools/rustfmt/tests/source/configs/indent_style/visual_where_pred.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-indent_style: Visual
// Where predicate indent

fn lorem<Ipsum, Dolor, Sit, Amet>() -> T where Ipsum: Eq, Dolor: Eq, Sit: Eq, Amet: Eq {
    // body
}


