tests/ui/manual/manual-link-bad-kind.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-l bar=foo
// error-pattern: unknown library kind `bar`, expected one of: static, dylib, framework, link-arg

fn main() {
}


