tests/ui/moves/move-out-of-field.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::string::String;

struct StringBuffer {
    s: String,
}

impl StringBuffer {
    pub fn append(&mut self, v: &str) {
        self.s.push_str(v);
    }
}

fn to_string(sb: StringBuffer) -> String {
    sb.s
}

pub fn main() {
    let mut sb = StringBuffer {
        s: String::new(),
    };
    sb.append("Hello, ");
    sb.append("World!");
    let str = to_string(sb);
    assert_eq!(str, "Hello, World!");
}


