tests/ui/mismatched_types/issue-75361-mismatched-impl.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regresison test for issue #75361
// Tests that we don't ICE on mismatched types with inference variables


trait MyTrait {
    type Item;
}

pub trait Graph {
  type EdgeType;

  fn adjacent_edges(&self) -> Box<dyn MyTrait<Item = &Self::EdgeType>>;
}

impl<T> Graph for T {
  type EdgeType = T;

  fn adjacent_edges(&self) -> Box<dyn MyTrait<Item = &Self::EdgeType> + '_> { //~ ERROR `impl`
      panic!()
  }

}

fn main() {}


