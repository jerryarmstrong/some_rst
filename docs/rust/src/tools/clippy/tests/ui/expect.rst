src/tools/clippy/tests/ui/expect.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::expect_used)]

fn expect_option() {
    let opt = Some(0);
    let _ = opt.expect("");
}

fn expect_result() {
    let res: Result<u8, u8> = Ok(0);
    let _ = res.expect("");
    let _ = res.expect_err("");
}

fn main() {
    expect_option();
    expect_result();
}


