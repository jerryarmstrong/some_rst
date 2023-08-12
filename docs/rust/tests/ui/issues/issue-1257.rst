tests/ui/issues/issue-1257.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

pub fn main () {
  let mut line = "".to_string();
  let mut i = 0;
  while line != "exit".to_string() {
    line = if i == 9 { "exit".to_string() } else { "notexit".to_string() };
    i += 1;
  }
}


