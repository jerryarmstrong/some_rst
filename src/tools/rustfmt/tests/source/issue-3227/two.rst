src/tools/rustfmt/tests/source/issue-3227/two.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-version: Two

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


