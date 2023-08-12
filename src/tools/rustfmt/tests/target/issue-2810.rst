src/tools/rustfmt/tests/target/issue-2810.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-newline_style: Windows

#[macro_export]
macro_rules! hmmm___ffi_error {
    ($result:ident) => {
        pub struct $result {
            success: bool,
        }

        impl $result {
            pub fn foo(self) {}
        }
    };
}


