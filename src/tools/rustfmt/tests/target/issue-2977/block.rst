src/tools/rustfmt/tests/target/issue-2977/block.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! atomic_bits {
    ($ldrex:expr) => {
        execute(|| {
            asm!($ldrex
                 : "=r"(raw)
                 : "r"(address)
                 :
                 : "volatile");
        })
    };
}


