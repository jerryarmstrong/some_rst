tests/ui/async-await/unnecessary-await.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

async fn foo () { }
fn bar() -> impl std::future::Future { async {} }
fn boo() {}

async fn baz() -> std::io::Result<()> {
    foo().await;
    boo().await; //~ ERROR `()` is not a future
    bar().await;
    std::io::Result::Ok(())
}

fn main() {}


