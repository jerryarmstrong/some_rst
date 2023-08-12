src/tools/rustfmt/tests/target/configs/indent_style/block_tab_spaces_call.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-indent_style: Block
// rustfmt-max_width: 80
// rustfmt-tab_spaces: 2

// #1427
fn main() {
  exceptaions::config(move || {
    (
      NmiConfig {},
      HardFaultConfig {},
      SysTickConfig { gpio_sbsrr },
    )
  });
}


