src/tools/rustfmt/tests/target/issue-3217.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut res = 0;
    's_39: {
        if res == 0i32 {
            println!("Hello, world!");
        }
    }
    's_40: loop {
        println!("res = {}", res);
        res += 1;
        if res == 3i32 {
            break 's_40;
        }
    }
    let toto = || {
        if true {
            42
        } else {
            24
        }
    };
}


