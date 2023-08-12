src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0106_lambda_expr.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    || ();
    || -> i32 { 92 };
    |x| x;
    move |x: i32,| x;
    async || {};
    move || {};
    async move || {};
    static || {};
    static move || {};
    static async || {};
    static async move || {};
    for<'a> || {};
    for<'a> move || {};
}


