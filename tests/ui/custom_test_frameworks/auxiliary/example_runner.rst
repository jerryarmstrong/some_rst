tests/ui/custom_test_frameworks/auxiliary/example_runner.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Testable {
    fn name(&self) -> String;
    fn run(&self) -> Option<String>; // None will be success, Some is the error message
}

pub fn runner(tests: &[&dyn Testable]) {
    for t in tests {
        print!("{}........{}", t.name(), t.run().unwrap_or_else(|| "SUCCESS".to_string()));
    }
}


