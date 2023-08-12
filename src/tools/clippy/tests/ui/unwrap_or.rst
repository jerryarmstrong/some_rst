src/tools/clippy/tests/ui/unwrap_or.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::all, clippy::or_fun_call)]

fn main() {
    let s = Some(String::from("test string")).unwrap_or("Fail".to_string()).len();
}

fn new_lines() {
    let s = Some(String::from("test string")).unwrap_or("Fail".to_string()).len();
}


