tests/ui/sanitize/leak.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-sanitizer-support
// needs-sanitizer-leak
//
// compile-flags: -Z sanitizer=leak -O
//
// run-fail
// error-pattern: LeakSanitizer: detected memory leaks

use std::hint::black_box;
use std::mem;

fn main() {
    for _ in 0..10 {
        let xs = vec![1, 2, 3];
        // Prevent compiler from removing the memory allocation.
        let xs = black_box(xs);
        mem::forget(xs);
    }
}


