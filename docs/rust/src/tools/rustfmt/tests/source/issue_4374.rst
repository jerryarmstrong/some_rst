src/tools/rustfmt/tests/source/issue_4374.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a<F>(_f: F) -> ()
where
  F: FnOnce() -> (),
{
}
fn main() {
  a(|| {
    #[allow(irrefutable_let_patterns)]
    while let _ = 0 {
      break;
    }
  });
}

