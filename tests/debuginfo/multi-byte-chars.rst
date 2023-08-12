tests/debuginfo/multi-byte-chars.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // min-lldb-version: 310

// compile-flags:-g

// This test checks whether debuginfo generation can handle multi-byte UTF-8
// characters at the end of a block. There's no need to do anything in the
// debugger -- just make sure that the compiler doesn't crash.
// See also issue #18791.

struct C { θ: u8 }

fn main() {
    let x =  C { θ: 0 };
    (|c: C| c.θ )(x);
}


