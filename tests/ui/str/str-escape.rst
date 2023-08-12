tests/ui/str/str-escape.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
fn main() {
    let s = "\

             ";
    //~^^^ WARNING multiple lines skipped by escaped newline
    let s = "foo\
             bar
             ";
    //~^^^ WARNING non-ASCII whitespace symbol '\u{a0}' is not skipped
}


