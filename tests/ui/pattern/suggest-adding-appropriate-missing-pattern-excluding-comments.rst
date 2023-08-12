tests/ui/pattern/suggest-adding-appropriate-missing-pattern-excluding-comments.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    match Some(1) { //~ ERROR non-exhaustive patterns: `None` not covered
        Some(1) => {}
        // hello
        Some(_) => {}
    }
}


