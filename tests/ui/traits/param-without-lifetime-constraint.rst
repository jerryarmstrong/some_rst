tests/ui/traits/param-without-lifetime-constraint.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Article {
    proof_reader: ProofReader,
}

struct ProofReader {
    name: String,
}

pub trait HaveRelationship<To> {
    fn get_relation(&self) -> To;
}

impl HaveRelationship<&ProofReader> for Article {
    fn get_relation(&self) -> &ProofReader {
    //~^ ERROR `impl` item signature doesn't match `trait` item signature
        &self.proof_reader
    }
}

fn main() {}


