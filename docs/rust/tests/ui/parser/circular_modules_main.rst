tests/ui/parser/circular_modules_main.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: circular modules

#[path = "circular_modules_hello.rs"]
mod circular_modules_hello;

pub fn hi_str() -> String {
    "Hi!".to_string()
}

fn main() {
    circular_modules_hello::say_hello();
}


