src/tools/rust-analyzer/crates/syntax/test_data/parser/validation/invalid_let_expr.rs
=====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    const _: () = let _ = None;

    let _ = if true { (let _ = None) };

    if true && (let _ = None) {
        (let _ = None);
        while let _ = None {
            match None {
                _ if let _ = None => { let _ = None; }
            }
        }
    }
}


