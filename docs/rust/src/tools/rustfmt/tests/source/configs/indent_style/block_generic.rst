src/tools/rustfmt/tests/source/configs/indent_style/block_generic.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-indent_style: Block
// Generics indent

fn lorem<Ipsum: Eq = usize, Dolor: Eq = usize, Sit: Eq = usize, Amet: Eq = usize, Adipiscing: Eq = usize, Consectetur: Eq = usize, Elit: Eq = usize>(ipsum: Ipsum, dolor: Dolor, sit: Sit, amet: Amet, adipiscing: Adipiscing, consectetur: Consectetur, elit: Elit) -> T {
    // body
}


