tests/ui/pattern/usefulness/issue-78549-ref-pat-and-str.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// From https://github.com/rust-lang/rust/issues/78549

fn main() {
    match "foo" {
        "foo" => {},
        &_ => {},
    }

    match "foo" {
        &_ => {},
        "foo" => {},
    }

    match ("foo", 0, "bar") {
        (&_, 0, &_) => {},
        ("foo", _, "bar") => {},
        (&_, _, &_) => {},
    }

    match (&"foo", "bar") {
        (&"foo", &_) => {},
        (&&_, &_) => {},
    }
}


