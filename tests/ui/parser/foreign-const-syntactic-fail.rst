tests/ui/parser/foreign-const-syntactic-fail.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Syntactically, a `const` item inside an `extern { ... }` block is not allowed.

fn main() {}

#[cfg(FALSE)]
extern "C" {
    const A: isize; //~ ERROR extern items cannot be `const`
    const B: isize = 42; //~ ERROR extern items cannot be `const`
}


