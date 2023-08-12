tests/ui/parser/stripped-nested-outline-mod-pass.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Expansion drives parsing, so conditional compilation will strip
// out outline modules and we will never attempt parsing them.

// check-pass

fn main() {}

#[cfg(FALSE)]
mod foo {
    mod bar {
        mod baz; // This was an error before.
    }
}


