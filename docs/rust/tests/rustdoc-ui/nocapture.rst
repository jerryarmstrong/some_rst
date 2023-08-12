tests/rustdoc-ui/nocapture.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags:--test -Zunstable-options --nocapture
// normalize-stdout-test: "tests/rustdoc-ui" -> "$$DIR"
// normalize-stdout-test "finished in \d+\.\d+s" -> "finished in $$TIME"

/// ```
/// println!("hello!");
/// eprintln!("stderr");
/// ```
pub struct Foo;


