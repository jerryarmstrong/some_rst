tests/ui/structs-enums/class-str-field.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

// pretty-expanded FIXME #23616

struct cat {

  name : String,

}

fn cat(in_name: String) -> cat {
    cat {
        name: in_name
    }
}

pub fn main() {
  let _nyan = cat("nyan".to_string());
}


