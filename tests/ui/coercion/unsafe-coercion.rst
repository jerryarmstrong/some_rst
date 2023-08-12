tests/ui/coercion/unsafe-coercion.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Check that safe fns are not a subtype of unsafe fns.


fn foo(x: i32) -> i32 {
    x * 22
}

fn bar(x: fn(i32) -> i32) -> unsafe fn(i32) -> i32 {
    x // OK, coercion!
}

fn main() {
    let f = bar(foo);
    let x = unsafe { f(2) };
    assert_eq!(x, 44);
}


