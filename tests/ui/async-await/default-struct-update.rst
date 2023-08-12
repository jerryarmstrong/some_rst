tests/ui/async-await/default-struct-update.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// edition:2018
// compile-flags: -Zdrop-tracking=y

fn main() {
    let _ = foo();
}

async fn from_config(_: Config) {}

async fn foo() {
    from_config(Config {
        nickname: None,
        ..Default::default()
    })
    .await;
}

#[derive(Default)]
struct Config {
    nickname: Option<Box<u8>>,
}


