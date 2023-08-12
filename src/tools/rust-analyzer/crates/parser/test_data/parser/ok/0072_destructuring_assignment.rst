src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0072_destructuring_assignment.rs
==========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    let (mut a, mut b) = (0, 1);
    (b, a, ..) = (a, b);
    (_) = ..;
    struct S { a: i32 }
    S { .. } = S { ..S::default() };
    Some(..) = Some(0).
    Ok(_) = 0;
    let (a, b);
    [a, .., b] = [1, .., 2];
    (_, _) = (a, b);
    (_) = (a, b);
    _ = (a, b);
}


