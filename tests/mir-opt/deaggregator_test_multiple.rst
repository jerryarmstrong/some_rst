tests/mir-opt/deaggregator_test_multiple.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: Deaggregator
// Test that deaggregate fires more than once per block

enum Foo {
    A(i32),
    B,
}

// EMIT_MIR deaggregator_test_multiple.test.Deaggregator.diff
fn test(x: i32) -> [Foo; 2] {
    [Foo::A(x), Foo::A(x)]
}

fn main() {
    // Make sure the function actually gets instantiated.
    test(0);
}


