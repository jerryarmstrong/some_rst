tests/ui/issues/issue-19811-escape-unicode.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() {
    let mut escaped = String::from("");
    for c in '\u{10401}'.escape_unicode() {
        escaped.push(c);
    }
    assert_eq!("\\u{10401}", escaped);
}


