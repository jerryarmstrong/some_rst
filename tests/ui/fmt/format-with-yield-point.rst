tests/ui/fmt/format-with-yield-point.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2021

macro_rules! m {
    () => {
        async {}.await
    };
}

async fn with_await() {
    println!("{} {:?}", "", async {}.await);
}

async fn with_macro_call_expr() {
    println!("{} {:?}", "", m!());
}

async fn with_macro_call_stmt_semi() {
    println!("{} {:?}", "", { m!(); });
}

async fn with_macro_call_stmt_braced() {
    println!("{} {:?}", "", { m!{} });
}

fn assert_send(_: impl Send) {}

fn main() {
    assert_send(with_await());
    assert_send(with_macro_call_expr());
    assert_send(with_macro_call_stmt_semi());
    assert_send(with_macro_call_stmt_braced());
}


