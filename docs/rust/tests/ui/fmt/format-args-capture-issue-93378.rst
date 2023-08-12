tests/ui/fmt/format-args-capture-issue-93378.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a = "a";
    let b = "b";

    println!("{a} {b} {} {} {c} {}", c = "c");
    //~^ ERROR: 3 positional arguments in format string, but there is 1 argument

    let n = 1;
    println!("{a:.n$} {b:.*}");
    //~^ ERROR: 1 positional argument in format string, but no arguments were given
}


