src/tools/rustfmt/tests/target/issue-3227/one.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: One

fn main() {
    thread::spawn(|| {
        while true {
            println!("iteration");
        }
    });

    thread::spawn(|| loop {
        println!("iteration");
    });
}


