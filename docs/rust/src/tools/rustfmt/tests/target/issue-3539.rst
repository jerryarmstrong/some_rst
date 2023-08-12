src/tools/rustfmt/tests/target/issue-3539.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::io::Error;

fn main() {
    let _read_num: fn() -> Result<(i32), Error> = || -> Result<(i32), Error> {
        let a = 1;
        Ok(a)
    };
}


