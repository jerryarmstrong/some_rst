tests/ui/symbol-names/verbose.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #57596, where -Zverbose flag unintentionally
// affected produced symbols making it impossible to link between crates
// with a different value of the flag (for symbols involving generic
// arguments equal to defaults of their respective parameters).
//
// build-pass
// compile-flags: -Zverbose

pub fn error(msg: String) -> Box<dyn std::error::Error> {
  msg.into()
}

fn main() {
  error(String::new());
}


