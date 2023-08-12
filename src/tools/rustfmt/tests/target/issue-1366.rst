src/tools/rustfmt/tests/target/issue-1366.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    fn f() -> Option<i32> {
        Some("fffffffsssssssssddddssssfffffddddff")
            .map(|s| s)
            .map(|s| s.to_string())
            .map(|res| match Some(res) {
                Some(ref s) if s == "" => 41,
                Some(_) => 42,
                _ => 43,
            })
    }
    println!("{:?}", f())
}


