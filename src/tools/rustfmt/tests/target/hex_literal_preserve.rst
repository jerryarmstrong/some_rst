src/tools/rustfmt/tests/target/hex_literal_preserve.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-hex_literal_case: Preserve
fn main() {
    let h1 = 0xcAfE_5Ea7;
    let h2 = 0xCaFe_F00du32;
}


