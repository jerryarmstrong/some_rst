compiler/rustc_codegen_gcc/tests/lang_tests_release.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod lang_tests_common;

fn main() {
    lang_tests_common::main_inner(lang_tests_common::Profile::Release);
}


