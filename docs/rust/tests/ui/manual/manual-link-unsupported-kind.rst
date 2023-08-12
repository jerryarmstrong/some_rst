tests/ui/manual/manual-link-unsupported-kind.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-l raw-dylib=foo
// error-pattern: unknown library kind `raw-dylib`, expected one of: static, dylib, framework, link-arg

fn main() {
}


