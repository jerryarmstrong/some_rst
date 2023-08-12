tests/ui/consts/min_const_fn/cast_fn.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {}

const fn unsize(x: &[u8; 3]) -> &[u8] { x }
const fn closure() -> fn() { || {} }
const fn closure2() {
    (|| {}) as fn();
}
const fn reify(f: fn()) -> unsafe fn() { f }
const fn reify2() { main as unsafe fn(); }


