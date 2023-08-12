tests/ui/lint/lint-pre-expansion-extern-module.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -W rust-2018-compatibility
// error-pattern: `try` is a keyword in the 2018 edition

fn main() {}

mod lint_pre_expansion_extern_module_aux;


