tests/mir-opt/deaggregator_test_enum.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: Deaggregator

enum Baz {
    Empty,
    Foo { x: usize },
}

// EMIT_MIR deaggregator_test_enum.bar.Deaggregator.diff
fn bar(a: usize) -> Baz {
    Baz::Foo { x: a }
}

fn main() {
    let x = bar(10);
    match x {
        Baz::Empty => println!("empty"),
        Baz::Foo { x } => println!("{}", x),
    };
}


