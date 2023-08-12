tests/ui/macros/pub-item-inside-macro.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Issue #14660

// pretty-expanded FIXME #23616

mod bleh {
    macro_rules! foo {
        () => {
            pub fn bar() { }
        }
    }

    foo!();
}

fn main() {
    bleh::bar();
}


