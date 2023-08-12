tests/ui/or-patterns/let-pattern.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn or_pat_let(x: Result<u32, u32>) -> u32 {
    let (Ok(y) | Err(y)) = x;
    y
}

fn or_pat_arg((Ok(y) | Err(y)): Result<u32, u32>) -> u32 {
    y
}

fn main() {
    assert_eq!(or_pat_let(Ok(3)), 3);
    assert_eq!(or_pat_let(Err(5)), 5);
    assert_eq!(or_pat_arg(Ok(7)), 7);
    assert_eq!(or_pat_arg(Err(9)), 9);
}


