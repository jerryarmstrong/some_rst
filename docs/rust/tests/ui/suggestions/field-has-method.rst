tests/ui/suggestions/field-has-method.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Kind;

struct Ty {
    kind: Kind,
}

impl Ty {
    fn kind(&self) -> Kind {
        todo!()
    }
}

struct InferOk<T> {
    value: T,
    predicates: Vec<()>,
}

fn foo(i: InferOk<Ty>) {
    let k = i.kind();
    //~^ no method named `kind` found for struct `InferOk` in the current scope
}

fn main() {}


