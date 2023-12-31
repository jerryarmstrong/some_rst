src/tools/clippy/tests/ui-toml/await_holding_invalid_type/await_holding_invalid_type.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::await_holding_invalid_type)]
use std::net::Ipv4Addr;

async fn bad() -> u32 {
    let _x = String::from("hello");
    baz().await
}

async fn bad_reason() -> u32 {
    let _x = Ipv4Addr::new(127, 0, 0, 1);
    baz().await
}

async fn good() -> u32 {
    {
        let _x = String::from("hi!");
        let _y = Ipv4Addr::new(127, 0, 0, 1);
    }
    baz().await;
    let _x = String::from("hi!");
    47
}

async fn baz() -> u32 {
    42
}

#[allow(clippy::manual_async_fn)]
fn block_bad() -> impl std::future::Future<Output = u32> {
    async move {
        let _x = String::from("hi!");
        baz().await
    }
}

fn main() {
    good();
    bad();
    bad_reason();
    block_bad();
}


