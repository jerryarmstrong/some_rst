tests/mir-opt/inline/inline_retag.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z span_free_formats -Z mir-emit-retag

// Tests that MIR inliner fixes up `Retag`'s `fn_entry` flag

fn main() {
    println!("{}", bar());
}

// EMIT_MIR inline_retag.bar.Inline.after.mir
fn bar() -> bool {
    let f = foo;
    f(&1, &-1)
}

#[inline(always)]
fn foo(x: &i32, y: &i32) -> bool {
    *x == *y
}


