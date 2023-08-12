src/tools/clippy/tests/ui/unwrap.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::unwrap_used)]

fn unwrap_option() {
    let opt = Some(0);
    let _ = opt.unwrap();
}

fn unwrap_result() {
    let res: Result<u8, u8> = Ok(0);
    let _ = res.unwrap();
    let _ = res.unwrap_err();
}

fn main() {
    unwrap_option();
    unwrap_result();
}


