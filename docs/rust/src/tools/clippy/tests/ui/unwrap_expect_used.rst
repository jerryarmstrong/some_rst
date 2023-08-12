src/tools/clippy/tests/ui/unwrap_expect_used.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::unwrap_used, clippy::expect_used)]

trait OptionExt {
    type Item;

    fn unwrap_err(self) -> Self::Item;

    fn expect_err(self, msg: &str) -> Self::Item;
}

impl<T> OptionExt for Option<T> {
    type Item = T;
    fn unwrap_err(self) -> T {
        panic!();
    }

    fn expect_err(self, msg: &str) -> T {
        panic!();
    }
}

fn main() {
    Some(3).unwrap();
    Some(3).expect("Hello world!");

    // Don't trigger on unwrap_err on an option
    Some(3).unwrap_err();
    Some(3).expect_err("Hellow none!");

    let a: Result<i32, i32> = Ok(3);
    a.unwrap();
    a.expect("Hello world!");
    a.unwrap_err();
    a.expect_err("Hello error!");
}


