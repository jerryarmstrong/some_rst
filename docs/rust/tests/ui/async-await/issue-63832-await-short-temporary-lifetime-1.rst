tests/ui/async-await/issue-63832-await-short-temporary-lifetime-1.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018

struct Test(String);

impl Test {
    async fn borrow_async(&self) {}

    fn with(&mut self, s: &str) -> &mut Self {
        self.0 = s.into();
        self
    }
}

async fn test() {
    Test("".to_string()).with("123").borrow_async().await;
}

fn main() { }


