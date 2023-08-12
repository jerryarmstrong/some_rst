tests/ui/mir/issue-76803-branches-not-same.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[derive(Debug, Eq, PartialEq)]
pub enum Type {
    A,
    B,
}


pub fn encode(v: Type) -> Type {
    match v {
        Type::A => Type::B,
        _ => v,
    }
}

fn main() {
  assert_eq!(Type::B, encode(Type::A));
}


