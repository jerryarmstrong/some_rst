src/tools/rustfmt/tests/target/issue-3759.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let Test {
        #[cfg(feature = "test")]
        x,
    } = Test {
        #[cfg(feature = "test")]
        x: 1,
    };

    let Test {
        #[cfg(feature = "test")]
        // comment
        x,
    } = Test {
        #[cfg(feature = "test")]
        x: 1,
    };

    let Test {
        // comment
        #[cfg(feature = "test")]
        x,
    } = Test {
        #[cfg(feature = "test")]
        x: 1,
    };
}


