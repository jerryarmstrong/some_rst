tests/ui/pattern/usefulness/issue-53820-slice-pattern-large-array.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// This used to cause a stack overflow during exhaustiveness checking in the compiler.

fn main() {
    const LARGE_SIZE: usize = 1024 * 1024;
    let [..] = [0u8; LARGE_SIZE];
    match [0u8; LARGE_SIZE] {
        [..] => {}
    }
}


