tests/mir-opt/inline/inline_closure_captures.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z span_free_formats

// Tests that MIR inliner can handle closure captures.

fn main() {
    println!("{:?}", foo(0, 14));
}

// EMIT_MIR inline_closure_captures.foo.Inline.after.mir
fn foo<T: Copy>(t: T, q: i32) -> (i32, T) {
    let x = |_q| (q, t);
    x(q)
}


