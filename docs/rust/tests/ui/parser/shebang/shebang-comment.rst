tests/ui/parser/shebang/shebang-comment.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #!//bin/bash

// check-pass
fn main() {
    println!("a valid shebang (that is also a rust comment)")
}


