src/tools/rustfmt/tests/target/issue-2554.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #2554
// Do not add the beginning vert to the first match arm's pattern.

fn main() {
    match foo(|_| {
        bar(|_| {
            //
        })
    }) {
        Ok(()) => (),
        Err(_) => (),
    }
}


