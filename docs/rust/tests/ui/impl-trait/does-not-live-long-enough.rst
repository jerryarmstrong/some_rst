tests/ui/impl-trait/does-not-live-long-enough.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct List {
    data: Vec<String>,
}
impl List {
    fn started_with<'a>(&'a self, prefix: &'a str) -> impl Iterator<Item=&'a str> {
        self.data.iter().filter(|s| s.starts_with(prefix)).map(|s| s.as_ref())
        //~^ ERROR E0373
    }
}

fn main() {}


