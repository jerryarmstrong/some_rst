tests/mir-opt/inline/inline_closure.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z span_free_formats

// Tests that MIR inliner can handle closure arguments. (#45894)

fn main() {
    println!("{}", foo(0, 14));
}

// EMIT_MIR inline_closure.foo.Inline.after.mir
fn foo<T: Copy>(_t: T, q: i32) -> i32 {
    let x = |_t, _q| _t;
    x(q, q)
}


