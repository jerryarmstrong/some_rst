tests/ui/borrowck/borrowck-fn-in-const-c.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we check fns appearing in constant declarations.
// Issue #22382.

// Returning local references?
struct DropString {
    inner: String
}
impl Drop for DropString {
    fn drop(&mut self) {
        self.inner.clear();
        self.inner.push_str("dropped");
    }
}
const LOCAL_REF: fn() -> &'static str = {
    fn broken() -> &'static str {
        let local = DropString { inner: format!("Some local string") };
        return &local.inner; //~ borrow may still be in use when destructor runs
    }
    broken
};

fn main() {
}


