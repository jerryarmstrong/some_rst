tests/ui/pattern/bindings-after-at/copy-and-move-mixed.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that mixing `Copy` and non-`Copy` types in `@` patterns is forbidden.

#[derive(Copy, Clone)]
struct C;

struct NC<A, B>(A, B);

fn main() {
    // this compiles
    let a @ NC(b, c) = NC(C, C);

    let a @ NC(b, c @ NC(d, e)) = NC(C, NC(C, C));
    //~^ ERROR use of partially moved value
}


