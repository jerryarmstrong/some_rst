src/tools/rustfmt/tests/target/issue-3494/crlf.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-file_lines: [{"file":"tests/source/issue-3494/crlf.rs","range":[4,5]}]

pub fn main() {
    let world1 = "world";
    println!("Hello, {}!", world1);
let world2 = "world"; println!("Hello, {}!", world2);
let world3 = "world"; println!("Hello, {}!", world3);
}


