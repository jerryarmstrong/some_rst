tests/ui/macros/must-use-in-macro-55516.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Wunused

// make sure write!() can't hide its unused Result

fn main() {
    use std::fmt::Write;
    let mut example = String::new();
    write!(&mut example, "{}", 42); //~WARN must be used
}


