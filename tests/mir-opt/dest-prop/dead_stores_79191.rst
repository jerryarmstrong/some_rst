tests/mir-opt/dest-prop/dead_stores_79191.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: DestinationPropagation

fn id<T>(x: T) -> T {
    x
}

// EMIT_MIR dead_stores_79191.f.DestinationPropagation.after.mir
fn f(mut a: usize) -> usize {
    let b = a;
    a = 5;
    a = b;
    id(a)
}

fn main() {
    f(0);
}


