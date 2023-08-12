src/tools/rustfmt/tests/target/async_closure.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-edition: 2018

fn main() {
    let async_closure = async {
        let x = 3;
        x
    };

    let f = async /* comment */ {
        let x = 3;
        x
    };

    let g = async /* comment */ move {
        let x = 3;
        x
    };

    let f = |x| async {
        println!("hello, world");
    };
}


