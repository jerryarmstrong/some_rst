tests/ui/issues/issue-3344.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(PartialEq)]
struct Thing(usize);
impl PartialOrd for Thing { //~ ERROR not all trait items implemented, missing: `partial_cmp`
    fn le(&self, other: &Thing) -> bool { true }
    fn ge(&self, other: &Thing) -> bool { true }
}
fn main() {}


