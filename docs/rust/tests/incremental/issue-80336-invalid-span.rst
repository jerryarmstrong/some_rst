tests/incremental/issue-80336-invalid-span.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #80336
// Test that we properly handle encoding, decoding, and hashing
// of spans with an invalid location and non-root `SyntaxContext`

// revisions:rpass1 rpass2
// only-x86_64

pub fn main() {
    let _ = is_x86_feature_detected!("avx2");
}


