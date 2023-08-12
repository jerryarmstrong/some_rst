tests/mir-opt/inline/inline_closure_borrows_arg.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z span_free_formats -Zunsound-mir-opts

// Tests that MIR inliner can handle closure arguments,
// even when (#45894)

fn main() {
    println!("{}", foo(0, &14));
}

// EMIT_MIR inline_closure_borrows_arg.foo.Inline.after.mir
fn foo<T: Copy>(_t: T, q: &i32) -> i32 {
    let x = |r: &i32, _s: &i32| {
        let variable = &*r;
        *variable
    };
    x(q, q)
}


