tests/ui/sanitize/address.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-sanitizer-support
// needs-sanitizer-address
//
// compile-flags: -Z sanitizer=address -O -g
//
// run-fail
// error-pattern: AddressSanitizer: stack-buffer-overflow
// error-pattern: 'xs' (line 13) <== Memory access at offset

use std::hint::black_box;

fn main() {
    let xs = [0, 1, 2, 3];
    // Avoid optimizing everything out.
    let xs = black_box(xs.as_ptr());
    let code = unsafe { *xs.offset(4) };
    std::process::exit(code);
}


