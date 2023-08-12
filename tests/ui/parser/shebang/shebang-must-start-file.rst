tests/ui/parser/shebang/shebang-must-start-file.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // something on the first line for tidy
#!/bin/bash  //~ expected `[`, found `/`

fn main() {
    println!("ok!");
}


