tests/ui/type-inference/or_else-multiple-type-params.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::process::{Command, Stdio};

fn main() {
    let process = Command::new("wc")
        .stdout(Stdio::piped())
        .spawn()
        .or_else(|err| { //~ ERROR type annotations needed
            panic!("oh no: {:?}", err);
        }).unwrap();
}


