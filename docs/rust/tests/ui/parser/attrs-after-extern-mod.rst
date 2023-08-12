tests/ui/parser/attrs-after-extern-mod.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure there's an error when given `extern { ... #[attr] }`.

fn main() {}

extern "C" {
    #[cfg(stage37)] //~ ERROR expected item after attributes
}


