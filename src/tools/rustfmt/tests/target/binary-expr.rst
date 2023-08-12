src/tools/rustfmt/tests/target/binary-expr.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Binary expressions

fn foo() {
    // 100
    let x = aaaaaaaaaa || bbbbbbbbbb || cccccccccc || dddddddddd && eeeeeeeeee || ffffffffff || ggg;
    // 101
    let x =
        aaaaaaaaaa || bbbbbbbbbb || cccccccccc || dddddddddd && eeeeeeeeee || ffffffffff || gggg;
    // 104
    let x = aaaaaaaaaa
        || bbbbbbbbbb
        || cccccccccc
        || dddddddddd && eeeeeeeeee
        || ffffffffff
        || gggggggg;
}


