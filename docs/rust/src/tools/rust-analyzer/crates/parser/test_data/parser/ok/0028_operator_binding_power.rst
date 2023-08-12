src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0028_operator_binding_power.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn binding_power() {
    let x = 1 + 2 * 3 % 4 - 5 / 6;
    1 + 2 * 3;
    1 << 2 + 3;
    1 & 2 >> 3;
    1 ^ 2 & 3;
    1 | 2 ^ 3;
    1 == 2 | 3;
    1 && 2 == 3;
    //1 || 2 && 2;
    //1 .. 2 || 3;
    //1 = 2 .. 3;
    //---&*1 - --2 * 9;
}


